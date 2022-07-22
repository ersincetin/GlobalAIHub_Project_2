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
    2: "Date range of Genre Type : ",
    3: "Films of English Record at BIGGEST IMBD Score : ",
    4: "\"Hindi\" Language Records' average of \"runtime\" : ",
    5: "\"Genre Column Details : \"",
    6: "Most use Three Language in DataSet : ",
    7: "Most Good IMDB Score 10 Films : ",
    8: "",
    9: "Most Good IMDB Score 10 Films of Genre : ",
    10: "Most Good Runtimes(sn) 10 Films : ",
    11: "which year of most films record : ",
    12: "Which language of lowest imdb score : (Note:all average then lowest)",
    13: "Which year of most sum \"runtimes\" : ",
    14: "Each Language of max use Genre Type :",
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


def daterange_genre_type_datas(start_date, end_date, genre_type):
    new_dataframe = numpy.array(dataframe.loc[(pandas.to_datetime(dataframe["Premiere"]) > start_date) & (
            pandas.to_datetime(dataframe["Premiere"]) <= end_date) & (dataframe["Genre"] == genre_type)])
    x = ["2019", "2020"]
    films_2019, films_2020 = 0, 0
    for item in new_dataframe:
        if item[2].find("-19") >= 0:
            films_2019 += 1
        elif item[2].find("-20") >= 0:
            films_2020 += 1
        else:
            continue
    pyplot.bar(x, [films_2019, films_2020], color="maroon", width=0.3)
    pyplot.title("Most Sum Runtime of Yearly")
    pyplot.show()


def most_sum_runtime_of_yearly():
    years = numpy.array(pandas.DatetimeIndex(dataframe["Premiere"]).year.value_counts().keys())
    biggest_runtime, sumRuntime, year_value = 0, 0, 0
    for year in years:
        sumRuntime = (dataframe.loc[(pandas.DatetimeIndex(dataframe["Premiere"]).year == year)])["Runtime"].sum()
        if biggest_runtime < sumRuntime:
            biggest_runtime = sumRuntime
            year_value = year
    print(f"The {year_value} is max sum runtime record.({biggest_runtime}sn)")


def each_language_of_genre_types():
    lang_items = list(dataframe["Language"].value_counts().keys())
    for item in list(dataframe["Language"].value_counts().keys()):
        if item.find("/") > 0:
            for language in item.split("/"):
                if language in lang_items:
                    continue
                else:
                    lang_items.append(language)
            lang_items.remove(item)
    for item in lang_items:
        print(
            f"{item} use most genre {numpy.array(dataframe.loc[lambda x: x['Language'].str.contains(item)]['Genre'].value_counts())[0]}.",
            end="\n\n")


def which_year_of_most_films():
    years = numpy.array(pandas.DatetimeIndex(dataframe["Premiere"]).year.value_counts().keys())
    biggest_films_count, year_item = 0, 0
    x, y = [], []
    for year in years:
        count = (dataframe.loc[(pandas.DatetimeIndex(dataframe["Premiere"]).year == year)])["Title"].count()
        if biggest_films_count < count:
            biggest_films_count = count
            year_item = year
        x.append(year)
        y.append(count)

    print(
        f"{year_item} record {biggest_films_count} most films.", end="\n\n")
    pyplot.bar(x, y, color="maroon", width=0.3)
    pyplot.title("Which year of Most Films Record")
    pyplot.show()


def which_language_lowest_imdb_score():
    lang_items = list(dataframe["Language"].value_counts().keys())
    for item in list(dataframe["Language"].value_counts().keys()):
        if item.find("/") > 0:
            for language in item.split("/"):
                if language in lang_items:
                    continue
                else:
                    lang_items.append(language)
            lang_items.remove(item)
    x, y = [], []
    imdb_score_sum = 0.0
    for lang in lang_items:
        x.append(lang)
        imdb_score_sum += float(dataframe.loc[lambda l: l['Language'].str.contains(lang)]['IMDB Score'].mean())
    imdb_score_average = imdb_score_sum / len(lang_items)
    for lang in lang_items:
        y.append(dataframe.loc[lambda l: l['Language'].str.contains(lang) & (l["IMDB Score"] < imdb_score_average)][
                     'IMDB Score'].mean())
    pyplot.bar(x, y, color="maroon", width=0.3)
    pyplot.title("Which language lowest imdb score")
    pyplot.show()


def select_step():
    for key, value in select_items.items():
        print(f"{key}->{value}")
    item_id = int(input("Please,Choose one : "))
    if item_id == 1:
        search_long_term_films()
    elif item_id == 2:
        daterange_genre_type_datas("01-2019", "06-2020", "Documentary")
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
    elif item_id == 11:
        which_year_of_most_films()
    elif item_id == 12:
        which_language_lowest_imdb_score()
    elif item_id == 13:
        most_sum_runtime_of_yearly()
    elif item_id == 14:
        each_language_of_genre_types()
    else:
        print("dont select")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    select_step()
