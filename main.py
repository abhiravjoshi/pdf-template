from fpdf import FPDF
import pandas as pd


def make_lines(pdf, start):
    line_size = 7
    for i in range(start, 297 - line_size, line_size):
        pdf.line(10, i, 200, i)


def main():
    df = pd.read_csv('topics.csv', )
    df = df.set_index('Order')
    pdf = FPDF(orientation='p', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=False, margin=0)
    # allows us to do align right footer
    for row_count, rows in df.iterrows():
        print_example = """       
        Topic    Default Arguments
        Pages                    2
        Name: 26, dtype: object
        """
        if rows['Pages'] > 1:
            for i in range(rows['Pages']):
                pdf.add_page()
                pdf.set_font(family="Times", style='b', size=24)
                pdf.set_text_color(100, 100, 100)
                # (R, G, B) tuple argument, closer to zero, the darker the color
                if i == 0:
                    # set header of first page
                    topics = rows['Topic']
                    pdf.cell(w=0, h=12, txt=topics, align='L', ln=1)
                    # pdf.line(10, 21, 200, 21)
                    make_lines(pdf, 21)
                    # set the footer:
                    pdf.ln(265)
                    pdf.set_font(family="Times", size=10)
                    pdf.set_text_color(180, 180, 180)
                    pdf.cell(w=0, h=10, txt=rows['Topic'], align='R')
                else:
                    make_lines(pdf, 14)
                    pdf.ln(277)
                    pdf.set_font(family="Times", size=10)
                    pdf.set_text_color(180, 180, 180)
                    pdf.cell(w=0, h=10, txt=rows['Topic'], align='R')
    pdf.output("output.pdf")


def for_fun():
    # these were some mess-ups I encountered while coding make_lines()
    # page 1
    pdf = FPDF(orientation='p', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font(family="Times", style='b', size=24)
    pdf.set_text_color(100, 100, 100)
    line_size = 7
    for i in range(21, 297 - line_size, line_size):
        pdf.line(i, 21, 200, line_size)

    # page 2
    pdf.add_page()
    pdf.set_font(family="Times", style='b', size=24)
    pdf.set_text_color(100, 100, 100)
    for i in range(21, 297 - line_size, line_size):
        pdf.line(10, i, 200, line_size)

    # page 3
    pdf.add_page()
    pdf.set_font(family="Times", style='b', size=24)
    pdf.set_text_color(100, 100, 100)
    for i in range(21, 297 - (line_size * 14), line_size):
        pdf.line(i, 21, 200, i)
        pdf.line(10, 21, i, i)
    pdf.output("output2.pdf")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    # for_fun()
