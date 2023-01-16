from fpdf import FPDF
import pandas as pd


def main():
    df = pd.read_csv('topics.csv', )
    df = df.set_index('Order')
    pdf = FPDF(orientation='p', unit='mm', format='letter')
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
                    topics = rows['Topic']
                    pdf.cell(w=0, h=12, txt=topics, align='L', ln=1)
                    pdf.line(10, 20, 206, 20)
                # pdf.footer()
    pdf.output("output.pdf")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
