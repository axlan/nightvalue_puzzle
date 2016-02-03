import markovgen
import textimage


file_ = open('combined')

markov = markovgen.Markov(file_)

txt = markov.generate_markov_text(100)

print txt

textimage.TextImage(txt,'test.jpg')
