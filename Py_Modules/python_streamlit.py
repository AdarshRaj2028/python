r"""
📘 PYTHON STREAMLIT MODULE: CONCEPTS, USAGE & BEST PRACTICES
======================================================================

--------------------------------------------------------------------------------
🔎 OVERVIEW
--------------------------------------------------------------------------------
* Streamlit is an open-source Python library for rapidly building interactive, web-based data apps.
* Ideal for prototyping, dashboards, ML demos, and data visualization.
* Simple Python scripts are rerun on user interaction; reactive and easy to use for non-web developers.

--------------------------------------------------------------------------------
1. INSTALLATION & IMPORT
--------------------------------------------------------------------------------
Installation:
    $ pip install streamlit

Import in script:
    import streamlit as st

Run your app:
    $ streamlit run your_script.py

Command-line help and info:
    $ streamlit --help

--------------------------------------------------------------------------------
2. IMPORTANT NOTICE ABOUT CACHING (st.cache DEPRECATION)
--------------------------------------------------------------------------------
* The `st.cache` decorator is **deprecated** and will be removed soon.
* Use the new decorators depending on your use case:
    - `@st.cache_data`: Cache functions that return *serializable data types*
      (e.g., DataFrames, arrays, lists, strings, numbers). This decorator copies the data on each call,
      protecting against unwanted mutations or concurrency bugs.
    - `@st.cache_resource`: Cache *resources* that are typically *not serializable*, such as ML models,
      database connections, and file handles. This caches the object itself and does **not** copy it,
      so mutations affect the cached object.
* Introduced in Streamlit 1.18 to improve clarity and safety.
* When migrating legacy apps, replace `@st.cache` accordingly.
* Read more: https://docs.streamlit.io/develop/concepts/architecture/caching

--------------------------------------------------------------------------------
3. DISPLAYING TEXT AND MARKDOWN
--------------------------------------------------------------------------------
* `st.text()`:
    - Displays fixed-width, plain text exactly as typed.
    - Does **not** parse formatting or markdown.
    - Good for showing code snippets or error messages.
* `st.markdown()`:
    - Parses and renders text written in Markdown syntax (see below).
    - Supports headings, bold, italic, lists, links, images, code blocks, blockquotes, tables.
    - Can optionally render raw HTML with `unsafe_allow_html=True` (use cautiously).
* st.subheader(): 
    - Displays a formatted secondary-level heading in a Streamlit app to organize content into clear subsections.
* `st.write()`:
    - Auto-detects content and displays it in appropriate format (text, dataframe, plot).
* `st.latex()`:
    - Renders LaTeX math equations for scientific notation.

**Markdown basics (supported in st.markdown):**

| Feature        | Syntax Example                | Description                       |
|----------------|-------------------------------|-----------------------------------|
| Heading 1      | `# Heading`                   | Large top-level header            |
| Bold           | `**bold**`                    | Bold text                         |
| Italic         | `_italic_` or `*italic*`      | Italicized text                   |
| Lists          | `- item` or `1. item`         | Bullet or numbered lists          |
| Link           | `[text](url)`                 | Hyperlinked text                  |
| Inline Code    | `` `code` ``                  | Inline code snippet               |
| Code Block     | <code>``````</code>           | Syntax-highlighted code block     |
| Blockquote     | `> quote`                     | Indented quote                    |
| Horizontal Rule| `---`                         | Horizontal line separator         |

--------------------------------------------------------------------------------
4. DISPLAYING DATA & CHARTS
--------------------------------------------------------------------------------
* `st.dataframe()`:
    - Interactive table, sortable and scrollable.
* `st.table()`:
    - Static table without interactivity.
* `st.json()`:
    - Pretty-prints JSON-like objects with syntax highlighting.
* Chart types:
    - Basic charts: `st.line_chart()`, `st.area_chart()`, `st.bar_chart()`
    - External libs supported: `st.pyplot()`, `st.altair_chart()`, `st.vega_lite_chart()`, `st.plotly_chart()`, `st.bokeh_chart()`
    - Map data: `st.map()`

--------------------------------------------------------------------------------
5. DISPLAYING MEDIA
--------------------------------------------------------------------------------
* Images: `st.image()`
* Audio: `st.audio()`
* Video: `st.video()
--------------------------------------------------------------------------------
6. INTERACTIVE WIDGETS
--------------------------------------------------------------------------------
- Return user interaction values for app logic.
- Examples: 
  - `st.button()`, `st.checkbox()`, `st.radio()`, `st.selectbox()`, `st.multiselect()`
  - `st.slider()`, `st.text_input()`, `st.number_input()`, `st.text_area()`
  - `st.date_input()`, `st.time_input()`, `st.file_uploader()`, `st.color_picker()`
- Sidebar widgets: Use `st.sidebar.<widget>()` or group inside `with st.sidebar:` for clean UI.

--------------------------------------------------------------------------------
7. PROGRESS, STATUS, & MESSAGES
--------------------------------------------------------------------------------
- `st.progress(value)`: Visual progress bar (0-100).
- `st.spinner(message)`: Show spinner with message during long operations.
- Status messages: `st.success()`, `st.info()`, `st.warning()`, `st.error()`
- Error display: `st.exception(e)` shows traceback.

--------------------------------------------------------------------------------
8. CODE DEBUGGING & FLOW
--------------------------------------------------------------------------------
- `st.stop()`: Halts app execution (useful during debugging).
- `st.echo()`: Shows Python code block executed in the app.

--------------------------------------------------------------------------------
9. PLACEHOLDERS & UPDATES
--------------------------------------------------------------------------------
- `st.empty()`: Create or reserve a UI placeholder dynamically updated.
- `st.help(obj)`: Shows Python docstring/help for any object.

--------------------------------------------------------------------------------
10. PAGE CONFIGURATION & OPTIONS
--------------------------------------------------------------------------------
- `st.set_page_config()`: Must be called once **at script top**; sets page title, layout ("wide"/"centered"), favicon, sidebar initial state.
- `st.get_option()` and `st.set_option()` modify Streamlit behaviors internally.

--------------------------------------------------------------------------------
11. LAYOUT MANAGEMENT
--------------------------------------------------------------------------------
- Use `st.columns(n)` to create multi-column layouts inside your app for horizontal UI.
- Sidebar is a vertical container separate from main page for navigation or filters.

--------------------------------------------------------------------------------
12. CACHING & PERFORMANCE
--------------------------------------------------------------------------------
- **Deprecated:** `@st.cache` replaced by two new decorators:
  - `@st.cache_data`: For caching data results from serializable functions (DataFrames, lists, strings, numbers).
    - Copies cached data on access, avoiding mutation/concurrency problems.
  - `@st.cache_resource`: For caching shared expensive resources (ML models, DB connections).
    - Returns same instance; mutations affect cached object globally.
- Use caching to speed up heavy computations, data queries, and loading.
- Control cache size/duration with `ttl` and `max_entries`.
- Customize spinner text with `show_spinner` parameter.

--------------------------------------------------------------------------------
13. SESSION STATE FOR INTERACTIVITY
--------------------------------------------------------------------------------
- `st.session_state`: Persistent dictionary that stores state between reruns.
- Ideal for multi-step workflows, counters, form states, toggles.
- Supports reactive state management inside your app.

--------------------------------------------------------------------------------
14. COMMON BEGINNER TIPS
--------------------------------------------------------------------------------
- Use `st.text()` for simple unformatted text.
- Use `st.markdown()` for rich text formatting.
- Utilize caching to optimize performance.
- Manage app flow and debugging with `st.stop()` and `st.echo()`.
- Leverage sidebar for separate controls, keep UI neat.
- Use session state for interactive and dynamic app experiences.
- Run apps locally using `streamlit run script.py`.

======================================================================
"""

# ================= RUNNABLE EXAMPLES ===================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# 0. Page config (top of your file)
st.set_page_config(
    page_title="Streamlit Concept Demo",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 1. Text and Markdown
st.title("Streamlit Concept Demo")
st.header("🖊️ Displaying Text and Markdown")
st.text('Fixed width text.')
st.markdown('_Markdown_ can be **bold** or _italic_.')
st.latex(r"(A + B)^2 = A^2 + 2AB + B^2")

# 2. Data Display
st.header("📊 Displaying Data")
data = pd.DataFrame(np.random.randn(10, 3), columns=['a', 'b', 'c'])
st.dataframe(data)
st.table(data.head(3))
st.json({'foo': 'bar', 'baz': [1, 2, 3]})

# 3. Charts
st.header("📈 Displaying Charts")
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 30, 25])
st.pyplot(fig)

# 4. Media
st.header("🖼️ Media Demo")
# st.image("path/to/image.jpg")  # Provide image path to test media display

# 5. Widgets Inside Main Area
st.header("⚡ Widgets")
if st.button('Say Hello'):
    st.write("Hello World!")
checked = st.checkbox('Check me out')
radio_val = st.radio('Choose one', [1, 2, 3])
selected = st.selectbox('Select one', ['A', 'B', 'C'])
multi = st.multiselect('Choose any', ['X', 'Y', 'Z'])
number = st.slider('Pick a number', 0, 100)
text = st.text_input('Say something:')
color = st.color_picker('Pick a color')
st.write('Your input:', text, 'Favorite color:', color)

# Sidebar widgets using container
with st.sidebar:
    st.header("Sidebar Widgets")
    side_val = st.text_input('Enter in sidebar:')
    side_button = st.button('Sidebar Button')
    if side_button:
        st.sidebar.write('You pressed sidebar button:', side_val)

# 6. Progress, spinners, and status
st.header("⏳ Status & Progress")
with st.spinner('Sleeping for 1 second...'):
    time.sleep(1)
st.success('Done!')

st.progress(70)
st.info('Information box')
st.warning('Warning box')
st.error('Error box')

try:
    _ = 1 / 0  # Intentionally cause division by zero
except Exception as e:
    st.exception(e)

# 7. Placeholders & Code Display
st.header("📦 Placeholders & Code Flow")
placeholder = st.empty()
placeholder.text("Temporary message...")
placeholder.markdown("**Updated message!**")

with st.echo():
    foo = 'bar'
    st.write(foo)

# Demonstrate st.stop() (Uncomment to test stopping execution)
# st.stop()
# st.write("This line will NOT run if st.stop() above is active.")

# 8. Cached Functions
st.header("⚙️ Caching Example")

@st.cache_data  # Use st.cache_data instead of deprecated st.cache
def expensive_computation(x):
    time.sleep(0.5)
    return x * x

st.write("Square of 4 cached:", expensive_computation(4))

# 9. File Upload with type filter
st.header("🗂️ File Uploader")
uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error reading file: {e}")

# 10. Layout with columns
st.header("🧱 Layout with Columns")
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1 content")
with col2:
    st.write("Column 2 content")

# 11. Session State demo
st.header("🧠 Session State Demo")
if 'count' not in st.session_state:
    st.session_state['count'] = 0

increment = st.button("Increment")
if increment:
    st.session_state['count'] += 1

st.write("Button clicked", st.session_state['count'], "times")

# =========== End of updated Streamlit concept file ===========
