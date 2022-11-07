import twint
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt
from MenuClass import menu
import nest_asyncio
nest_asyncio.apply()

def twint_to_pandas(columns):
    return twint.output.panda.Tweets_df[columns]

def append_sentiment():
    list_sentiment = []
    for tweet in df["tweet"]:
        analysis = TextBlob(tweet)
        if analysis.sentiment[0] > 0: list_sentiment.append(1.0)
        elif analysis.sentiment[0] < 0: list_sentiment.append(2.0)
        else: list_sentiment.append(0.0)
    df["Sentiment"] = list_sentiment

#Creación del dataframe
c = twint.Config()
c.Search = "Bayonetta"
c.Limit = 10
c.Pandas = True
twint.run.Search(c)
df = twint_to_pandas(["date", "username", "tweet", "hashtags", "nlikes"])
append_sentiment()




def show_dataframe():
    print(df)



def sentiment_graph_1():
    sns.distplot(df["Sentiment"])
    sns.set(rc={"figure.figsize": (10,6)})
    plt.show()
    print("Gráfico mostrado")
    

def sentiment_graph_2():
    df_new = df[["Sentiment"]].value_counts()
    df_new = df.groupby(['Sentiment']).count()
    df_new.nlikes.plot(kind="pie")
    plt.show()

def main():
    funciones =[
        show_dataframe, sentiment_graph_1,sentiment_graph_2
    ]

    opciones = [
        "Mostrar Dataframe con Tweets", "Gráfico histograma sentimientos", "Gráfico tarta sentimientos"
    ]

    my_menu = menu(funciones,opciones)

    while True:
        function = my_menu.select_menu()
        if function == -1: break
        else: function()
        input("Continue...")
    input("Thanks for using this menu")

if __name__ == "__main__":
    main()