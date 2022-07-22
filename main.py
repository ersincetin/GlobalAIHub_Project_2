import pandas
import numpy
import math
from matplotlib import pyplot

language_dict = {}
dataframe = pandas.read_csv("NetflixOriginals.csv", encoding='ISO-8859-1')
pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)
select_items = {
    1: "Which language of long terms ? :  ",
    2: "",
    3: "Films of English Record at BIGGEST IMBD Score : ",
    4: "\"Hindi\" Language Records' average of \"runtime\" : ",
    5: "\"Genre Column Details : \"",
    6: "Most use Three Language in DataSet : ",
    7: "Most Good IMDB Score 10 Films : ",
    8: "",
    9: "Most Good IMDB Score 10 Films of Genre : ",
    10: "Most Good Runtimes(sn) 10 Films : ",
    11: "",
    12: "",
    13: "Which year of most sum \"runtimes\" : ",
    14: "",
    15: ""
}


def search_long_term_films():
    data_array = numpy.array(dataframe)
    runtime_average = math.floor(dataframe["Runtime"].mean())
    lang_items = list(dataframe["Language"].value_counts().keys())
    for item in list(dataframe["Language"].value_counts().keys()):
        if item.find("/") > 0:
            for language in item.split("/"):
                if language in lang_items:
                    continue
                else:
                    lang_items.append(language)
            lang_items.remove(item)
    lang_count_dict = dict()
    for item in data_array:
        if runtime_average < int(item[3]):
            if item[5] in lang_count_dict:
                lang_count_dict[item[5]] = int(lang_count_dict[item[5]]) + 1
            else:
                lang_count_dict[item[5]] = 1
    pyplot.bar(lang_count_dict.keys(), lang_count_dict.values(), color="maroon", width=0.4)
    pyplot.title("Long Term Films")
    pyplot.show()


def films_of_english_record_IMDB():
    return numpy.array(dataframe)[
        (dataframe.loc[lambda x: x["Language"].str.contains("English") == True])["IMDB Score"].idxmax()]


def films_of_hindi_record_runtime_average():
    return (dataframe.loc[lambda x: x["Language"].str.contains("Hindi") == True])["Runtime"].mean()


def genre_column_details():
    genre_column = dataframe["Genre"].value_counts()
    pyplot.pie(numpy.array(genre_column))
    pyplot.title("Genre Column Details")
    pyplot.show()


def most_use_language(step):
    lang_items = list(dataframe["Language"].value_counts().keys())
    for item in list(dataframe["Language"].value_counts().keys()):
        if item.find("/") > 0:
            for language in item.split("/"):
                if language in lang_items:
                    continue
                else:
                    lang_items.append(language)
            lang_items.remove(item)
    lang_count_dict = dict()
    for item in numpy.array(dataframe):
        for list_item in item[5].split("/"):
            if list_item in lang_count_dict:
                lang_count_dict[list_item] = int(lang_count_dict[list_item]) + 1
            else:
                lang_count_dict[list_item] = 1
    sorted_most_use_language = sorted(lang_count_dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(step):
        print(f"{sorted_most_use_language[i][0]} language used {sorted_most_use_language[i][1]}.")


def most_good_imdb_score(step):
    film_items = numpy.array(dataframe.sort_values(by="IMDB Score", ascending=False).head(step))
    for i in range(step):
        print(
            f"Film name : {film_items[i][0]}\nGenre : {film_items[i][1]}\nPremiere : {film_items[i][2]}\nRuntime : {film_items[i][3]}\nIMDB Score : {film_items[i][4]}\nLanguage : {film_items[i][5]}",
            end="\n\n")


def most_good_imdb_score_of_genre(step):
    genres = numpy.array(dataframe.sort_values(by="IMDB Score", ascending=False).head(step))
    genres_items = dataframe.sort_values(by="IMDB Score", ascending=False)["Genre"].head(step).value_counts()
    for i in range(step):
        print(
            f"{i + 1}.Most Genre : {genres[i][1]}", end="\n")

    pyplot.bar(genres_items.keys(), genres_items.values, color="maroon", width=0.3)
    pyplot.title("Most Good IMDB Score of Genre")
    pyplot.show()


def most_good_runtime(step):
    film_items = numpy.array(dataframe.sort_values(by="Runtime", ascending=False).head(10))
    films = dict()
    for i in range(step):
        films[film_items[i][0]] = film_items[i][3]
        print(
            f"Film name : {film_items[i][0]}\nGenre : {film_items[i][1]}\nPremiere : {film_items[i][2]}\nRuntime : {film_items[i][3]}\nIMDB Score : {film_items[i][4]}\nLanguage : {film_items[i][5]}",
            end="\n\n")
    pyplot.bar(films.keys(), films.values(), color="maroon", width=0.4)
    pyplot.title(" ")
    pyplot.show()


def most_sum_runtime_of_yearly():
    date_times_values = dataframe.query("Premiere == 19-Agu-2019")
    print(date_times_values)


def select_step():
    for key, value in select_items.items():
        print(f"{key}->{value}")
    item_id = int(input("Please,Choose one : "))
    if item_id == 1:
        search_long_term_films()
    elif item_id == 3:
        print(films_of_english_record_IMDB())
    elif item_id == 4:
        print(f"\"Hindi\" Language Records' average of \"runtime\" : {films_of_hindi_record_runtime_average()} sn")
    elif item_id == 5:
        genre_column_details()
    elif item_id == 6:
        most_use_language(3)
    elif item_id == 7:
        most_good_imdb_score(10)
    elif item_id == 9:
        most_good_imdb_score_of_genre(10)
    elif item_id == 10:
        most_good_runtime(10)
    elif item_id == 13:
        most_sum_runtime_of_yearly()
    else:
        print("dont select")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    select_step()
