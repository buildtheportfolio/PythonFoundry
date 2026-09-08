import streamlit as st
import requests

st.set_page_config(
    page_title="Open Library Pro",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium UI Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

    :root {
        --primary: #6366f1;
        --primary-hover: #4f46e5;
        --bg-card: rgba(255, 255, 255, 0.05);
        --glass-border: rgba(255, 255, 255, 0.1);
    }

    * { font-family: 'Outfit', sans-serif; }

    .main .block-container { padding-top: 2rem; }

    /* Book Card Styling */
    .book-card {
        background: var(--bg-card);
        border: 1px solid var(--glass-border);
        border-radius: 16px;
        padding: 16px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        height: 100%;
        display: flex;
        flex-direction: column;
        backdrop-filter: blur(8px);
    }

    .book-card:hover {
        transform: translateY(-8px);
        border-color: var(--primary);
        box-shadow: 0 12px 24px rgba(0,0,0,0.2);
    }

    .cover-img {
        border-radius: 12px;
        width: 100%;
        aspect-ratio: 2/3;
        object-fit: cover;
        margin-bottom: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    .title-text {
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 4px;
        color: #f8fafc;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    .author-text {
        font-size: 0.9rem;
        color: #94a3b8;
        margin-bottom: 12px;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        transition: all 0.2s;
        border: 1px solid var(--glass-border);
    }

    .stButton > button:hover {
        border-color: var(--primary);
        color: var(--primary);
    }

    /* Detail Section */
    .detail-container {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        padding: 24px;
        margin-top: 2rem;
    }

    /* Tabs Customization */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px 4px 0px 0px;
        color: #94a3b8;
        font-weight: 600;
    }

    .stTabs [aria-selected="true"] {
        color: var(--primary) !important;
        border-bottom-color: var(--primary) !important;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data(show_spinner=False)
def search_books(query, page=1):
    try:
        url = f"https://openlibrary.org/search.json?q={query}&page={page}"
        res = requests.get(url, timeout=10)
        return res.json()
    except Exception as e:
        return {"error": str(e)}

@st.cache_data(show_spinner=False)
def get_book_details(key):
    try:
        url = f"https://openlibrary.org{key}.json"
        res = requests.get(url, timeout=10)
        return res.json()
    except Exception as e:
        return {"error": str(e)}

# Sidebar
with st.sidebar:
    st.title("📚 Library Settings")
    limit = st.slider("Display Results", 8, 40, 20)
    st.divider()
    
    if st.button("✨ Clear Search Cache"):
        st.cache_data.clear()
        st.success("Cache cleared!")

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "page" not in st.session_state:
    st.session_state.page = 1

# Main Header
st.markdown("<h1 style='text-align: center; color: #6366f1; font-weight: 800; font-size: 3rem;'>Open Library Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 1.2rem; margin-bottom: 2rem;'>The ultimate explorer for the world's largest open book database.</p>", unsafe_allow_html=True)

query = st.text_input("Search", placeholder="Search by title, author, or ISBN...", label_visibility="collapsed")

if query:
    if "last_query" not in st.session_state or st.session_state.last_query != query:
        st.session_state.page = 1
        st.session_state.last_query = query

    with st.spinner("Searching chronicles..."):
        data = search_books(query, st.session_state.page)

    if "error" in data:
        st.error(f"Failed to connect to the library: {data['error']}")
    else:
        books = data.get("docs", [])[:limit]

        if not books:
            st.warning("No books found matching your criteria.")
        else:
            cols = st.columns(4)

            for i, book in enumerate(books):
                col = cols[i % 4]
                with col:
                    title = book.get("title", "No title")
                    authors = ", ".join(book.get("author_name", ["Unknown"]))
                    cover_id = book.get("cover_i")
                    key = book.get("key")

                    st.markdown(f"""
                    <div class="book-card">
                        <img src="{"https://covers.openlibrary.org/b/id/" + str(cover_id) + "-M.jpg" if cover_id else "https://via.placeholder.com/200x300?text=No+Cover"}" class="cover-img">
                        <div class="title-text">{title}</div>
                        <div class="author-text">{authors}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    btn_cols = st.columns([1, 1])
                    with btn_cols[0]:
                        if st.button("Details", key=f"d{i}", use_container_width=True):
                            with st.spinner("Loading details..."):
                                details = get_book_details(key)
                                st.session_state["modal"] = details
                                st.session_state["active_book"] = book

                    with btn_cols[1]:
                        is_fav = any(f.get('key') == key for f in st.session_state.favorites)
                        if st.button("❤" if is_fav else "♡", key=f"f{i}", use_container_width=True):
                            if is_fav:
                                st.session_state.favorites = [f for f in st.session_state.favorites if f.get('key') != key]
                            else:
                                st.session_state.favorites.append(book)
                            st.rerun()

            # Pagination
            st.markdown("<br>", unsafe_allow_html=True)
            pcols = st.columns([1, 2, 1])
            with pcols[0]:
                if st.button("⬅ Previous Page") and st.session_state.page > 1:
                    st.session_state.page -= 1
                    st.rerun()
            with pcols[1]:
                st.markdown(f"<div style='text-align:center; padding: 10px; font-weight: 600; color: #94a3b8;'>Page {st.session_state.page}</div>", unsafe_allow_html=True)
            with pcols[2]:
                if st.button("Next Page ➡"):
                    st.session_state.page += 1
                    st.rerun()

# Detail View
if "modal" in st.session_state:
    st.divider()
    m = st.session_state["modal"]
    b = st.session_state["active_book"]
    
    with st.container():
        st.markdown("<div class='detail-container'>", unsafe_allow_html=True)
        dc1, dc2 = st.columns([1, 2])
        
        with dc1:
            cover_id = b.get("cover_i")
            if cover_id:
                st.image(f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg", use_container_width=True)
            else:
                st.warning("No high-resolution cover available.")
        
        with dc2:
            st.header(m.get("title", b.get("title")))
            st.subheader(", ".join(b.get("author_name", ["Unknown"])))
            
            # Description
            desc = m.get("description")
            if isinstance(desc, dict):
                desc = desc.get("value")
            
            if desc:
                st.markdown(desc)
            else:
                st.caption("No description available for this edition.")
            
            st.divider()
            
            # Metadata
            m_cols = st.columns(3)
            m_cols[0].metric("Published", b.get("first_publish_year", "N/A"))
            m_cols[1].metric("Pages", b.get("number_of_pages_median", "N/A"))
            m_cols[2].metric("Ebooks", "Yes" if b.get("has_fulltext") else "No")
            
            if "subjects" in m:
                st.markdown("**Subjects:**")
                st.write(", ".join(m["subjects"][:10]))
                
        st.markdown("</div>", unsafe_allow_html=True)

# Favorites Section
st.divider()
st.subheader("⭐ Your Favorites")

if st.session_state.favorites:
    fav_cols = st.columns(min(len(st.session_state.favorites), 6))
    for idx, fav in enumerate(st.session_state.favorites):
        with fav_cols[idx % 6]:
            cid = fav.get("cover_i")
            if cid:
                st.image(f"https://covers.openlibrary.org/b/id/{cid}-S.jpg", use_container_width=True)
            st.caption(fav.get("title")[:30] + "..." if len(fav.get("title")) > 30 else fav.get("title"))
else:
    st.info("You haven't saved any books to your favorites yet. Heart some books to see them here!")

st.markdown("<br><hr><p style='text-align: center; color: #64748b; font-size: 0.8rem;'>Powered by Open Library API · Built with Streamlit</p>", unsafe_allow_html=True)

