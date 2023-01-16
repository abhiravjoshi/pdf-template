from fpdf import FPDF
import pandas as pd


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
                pdf.set_font(family="Times", style='b', size=12)
                pdf.set_text_color(100, 100, 100)
                # (R, G, B) tuple argument, closer to zero, the darker the color
                if i == 0:
                    # set header of first page
                    topics = rows['Topic']
                    pdf.cell(w=0, h=12, txt=topics, align='L', ln=1)
                    pdf.line(10, 21, 200, 21)
                    # set the footer:
                    pdf.ln(265)
                    pdf.set_font(family="Times", size=10)
                    pdf.set_text_color(180, 180, 180)
                    pdf.cell(w=0, h=10, txt=rows['Topic'], align='R')
                else:
                    pdf.ln(277)
                    pdf.set_font(family="Times", size=10)
                    pdf.set_text_color(180, 180, 180)
                    pdf.cell(w=0, h=10, txt=rows['Topic'], align='R')


    pdf.output("output.pdf")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
