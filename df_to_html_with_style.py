class Df2HtmlWithStyle:
    def __init__(self, raw_df, output_html_path):
        df_style = raw_df.style
        for i, row in enumerate(raw_df.index):
            for j, col in enumerate(raw_df.columns):
                if j % 2:
                    df_style.applymap(lambda x: "background-color:e6ffe6;", subset=(slice(row), col))
                else:
                    df_style.applymap(lambda x: "background-color:D9C9E5;", subset=(slice(row), col))

        cell_hover = {  # for row hover use <tr> instead of <td>
            'selector': 'tr:hover',
            'props': 'color:magenta; text-align:center;',
        }
        index_names = {
            'selector': 'th',
            'props': 'font-style: italic; color: blue;'
                     'font-weight:normal; background-color: 87A06B;'
                     # 'position: sticky; left: 0px;'
        }
        headers = {
            'selector': 'th:not(.index_name)',
            'props': 'background-color: #A274AB; color: 122856;'
                     'position: sticky; left: 0px;'
                     'border: 1px solid black;'
                     'border-collapse: collapse;'
        }

        df1 = df_style.set_table_styles([
            # cell,
            index_names,
            headers,
            cell_hover,
        ]).\
            set_sticky(axis="index")
        # df1 = df.style.use(color_df_style.export())

        # html_relative_path = "hello1.html"
        with open(output_html_path, 'w') as html_writer:
            html_str = df1.render(). \
                replace('</style>', '</style>\n<form method="POST" action="save_data/{{ current_hour }}">'). \
                replace('</table>', '</table>\n</form>').replace('white', 'ABC9A6')

            html_writer.write(html_str)
        print(f'saved at {output_html_path}')
