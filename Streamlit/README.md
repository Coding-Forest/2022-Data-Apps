
## HTML components

  - `st.title()`
  - `st.subheader()`

  - `st.checkbox()`
  - `st.selectbox()`
  - `st.button()`
  - `st.text_area()`

  - `st.success()`    # displays successful result (like in console)
  - `st.warning()`
  - `st.text()`
  - `st.json()`       # returns data in json format

<br>

## NLP

  - `lemma    = [(token.text, token.lemma_) for entity in nlp(input_text)]`
  - `entities = [(entity.text, entity.label_) for entity in nlp(input_text).ents]`
  - `summary = [str(sent) for sent in LexRankSummarizer(parser.document, 3)]`

<br>

## Syntax

  - `if st.checkbox(box_content):`  == if checkbox is true
