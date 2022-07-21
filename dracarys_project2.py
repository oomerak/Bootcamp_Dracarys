"""

PYTBTCMP-30_Dracarys_Project2.py

"""

import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import time
sns.set(rc = {"figure.figsize": (10, 5)})

data = pd.read_csv("NetflixOriginals.csv", encoding='latin-1')


"""
data.isnull().sum()
data.info()
print(data.duplicated().sum())
data.describe().T
"""
for x in ["Runtime", "IMDB Score"]:
    q75,q25 = np.percentile(data.loc[:,x],[75,25])
    intr_qr = q75-q25
 
    max = q75+(1.5*intr_qr)
    min = q25-(1.5*intr_qr)
 
    data.loc[data[x] < min,x] = np.nan
    data.loc[data[x] > max,x] = np.nan

data = data.dropna(axis = 0)


"""
data.isnull().sum()
data.isnull().sum()
data.describe().T
"""


class notinListError(ValueError):
    pass

class exitPassError(ValueError):
    pass

class numberInputError(ValueError):
    pass


questions_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#To query the input value for catching error
def notinList(process):
    process2 = int(process)
    if process2 not in questions_list:
        raise notinListError
    else:
        pass
def exitPass(process):
    if process == "E" or process == "e":
        raise exitPassError
    else:
        pass
def numberInput(process):
    if all(chr.isdigit() for chr in process) == True:
        pass
    else:
        raise numberInputError

class questions():
    # Q1 - Veri setine göre uzun soluklu filmler hangi dilde oluşturulmuştur? Görselleştirme yapınız.
    def question1():
        full_length = data[data["Runtime"] > 90]
        full_lang = full_length.Language.value_counts()
        fig = px.pie(full_lang, names=full_lang.index, values=full_lang.values, title='Feature-length Movies')
        fig.show()

    # Q2 - 2019 Ocak ile 2020 Haziran tarihleri arasında 'Documentary' türünde çekilmiş filmlerin IMDB değerlerini bulup görselleştiriniz.
    def question2():
        type(data['Premiere'])
        data['Premiere'] = pd.to_datetime(data.Premiere)
        docIMDB = data[("2018-12-31" < data['Premiere']) & (data['Premiere'] < "2020-7-1")]    
        docIMDB=docIMDB.query("Genre == 'Documentary'")
        docIMDB.plot.scatter("Premiere","IMDB Score",color = {"red"})
        plt.xlabel("Premiere")
        plt.ylabel("IMDB Score")
        plt.title("Documentary")
        plt.show()

        


    # Q3 - İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?
    def question3():
        EngIMBD=data.query("Language == 'English'")
        colors = ['lightslategray',] * len(EngIMBD)
        colors[0:1] = ['crimson', "crimson"]
        EngIMBD = EngIMBD.sort_values(by=['IMDB Score'], axis=0, ascending=False)
        EngIMBD = EngIMBD.head()
        EngIMBD.plot.bar(x="Genre", y="IMDB Score", color=colors ,  )
        plt.subplots_adjust(
            top=0.925,
            bottom=0.320,
            left=0.125,
            right=0.9,
            hspace=0.2,
            wspace=0.2
        )
        plt.xlabel("Genre")
        plt.xticks(rotation=45)
        plt.ylabel("IMDB Score")
        plt.title("Top IMDB Scores of Movies in Englsih")
        plt.show()
        
    # Q4 - 'Hindi' Dilinde çekilmiş olan filmlerin ortalama 'runtime' suresi nedir?
    def question4():
        HindRun = data.query("Language == 'Hindi'")
        #HindRun2 = []
        HindRun = HindRun["Runtime"].mean()
        print(HindRun)

    # Q5 - 'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz.
    def question5():
        genre = data.Genre.value_counts().nlargest(20)  # genre = df['Genre'].value_counts()[:20]
        fig = px.bar(data_frame=genre, x=genre.index, y=genre.values, labels={"y":"Number of Movies from the Genre", "index":"Genres"})
        fig.update_layout(xaxis={"categoryorder":"total descending"})
        fig.show()

    # Q6 - Veri setinde bulunan filmlerde en çok kullanılan 3 dili bulunuz.
    def question6():
        TopLanguage = data['Language'].value_counts()
        colors = ['lightslategray',] * 3
        TopLanguage[0:3].plot.bar(x="Language", color = colors ) 
        plt.subplots_adjust(
            top=0.895,
            bottom=0.205,
            left=0.125,
            right=0.9,
            hspace=0.2,
            wspace=0.2
        )
        plt.xlabel("Language")
        plt.ylabel("Count")
        plt.title("The Most Used 3 Languages in Dataset")
        plt.xticks(rotation=45)
        plt.show()

    # Q7 - IMDB puanı en yüksek olan ilk 10 film hangileridir? Görselleştirin.
    def question7():
        IMDB10 = data.sort_values(by=['IMDB Score'], axis=0, ascending=False)
        print(IMDB10[0:10])

        IMDB10[0:10].plot.bar(x="Title", y="IMDB Score", color={"#a98d19"}, ylim=(8,8.7))
        plt.subplots_adjust(
            top=0.895,
            bottom=0.45,
            left=0.115,
            right=0.895,
            hspace=0.2,
            wspace=0.2
        )
        plt.xlabel("Movie Name")
        plt.ylabel("IMDB Score")
        plt.title("Top 10 Movie With High IMDB Score")
        plt.xticks(rotation=80)
        plt.show()

    # Q8 - IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz.
    def question8():
        corr = data["IMDB Score"].corr(data["Runtime"])
        print("Correlation between ", ["IMDB Score"], " and ", ["Runtime"], "is: ", round(corr, 2))
        sns.heatmap(data.corr("pearson"),cmap="Reds", annot=True , vmin= -1, vmax=1, square=True,
            linewidth=0.3, cbar_kws={"shrink": .8})
        plt.show()
    
    # Q9 IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz.
    def question9():
        IMDB10Genre = data.sort_values(by=['IMDB Score'], axis=0, ascending=False)
        IMDB10Genre = IMDB10Genre.groupby(["Genre"])[["IMDB Score"]].agg("max").sort_values(["IMDB Score"] , ascending=False)
        IMDB10Genre = IMDB10Genre.head(10)
        #IMDB10Genre.plot.bar(x="Genre", y="IMDB Score", color={"#a98d19"})
        IMDB10Genre.plot.bar(color={'crimson'}, figsize=(5,10)) 
        plt.xlabel("Genre")
        #ax1.legend(loc=2,fontsize=20)
        plt.subplots_adjust(
            top=0.952,
            bottom=0.36,
            left=0.096,
            right=0.943,
            hspace=0.2,
            wspace=0.2
        )
        plt.xticks(rotation=55)
        plt.ylabel("IMDB Score")
        plt.title("Top 10 IMDB Scores-Genre")
        plt.tight_layout()
        plt.show()
        
    # Q10 - 'Runtime' değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz.
    def question10():
        Run10Title = data.sort_values(by=['Runtime'], axis=0, ascending=False)
        Run10Title[0:10].plot.bar(x="Title", y="Runtime", color={"#a98d19"}, ylim=(130,142))
        plt.xlabel("Movie Name")
        plt.ylabel("Runtime")
        plt.title("Top 10 Movies with the Highest Runtime")
        plt.subplots_adjust(
            top=0.92,
            bottom=0.375,
            left=0.07,
            right=0.935,
            hspace=0.21,
            wspace=0.2
        )
        plt.show()

    # Q11 - Hangi yılda en fazla film yayımlanmıştır? Görselleştiriniz.
    def question11():
        data2 = data
        
        data2["Premiere"] = pd.to_datetime(data2["Premiere"])
        data2['Premiere'] = data2['Premiere'].dt.strftime("%Y")
        a = data2['Premiere'].value_counts()
        colors = ['lightslategray',] * len(a)
        colors[0] = "crimson"
        a.plot.bar(x="Premiere", color=colors)
        plt.xlabel("Year")
        plt.ylabel("Total Amount of Movies")
        plt.title("Years and Amount of Movies")
        plt.tight_layout()
        plt.show()

    # Q12 - Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir? Görselleştiriniz.
    def question12():
        IMDBlang = data[["Language" , "IMDB Score"]]
        IMDBlang= IMDBlang.groupby(['Language']).mean()
        IMDBlang=IMDBlang.sort_values(ascending=True,by=["IMDB Score"])
        IMDBlang.plot.bar(color={"crimson"})
        plt.xlabel("Languages")
        plt.ylabel("IMDB Score")
        plt.title("Distribution of Average IMDB Scores by Language")
        plt.subplots_adjust(
            top=0.913,
            bottom=0.337,
            left=0.05,
            right=0.982,
            hspace=0.2,
            wspace=0.2
        )
        plt.show()

    # Q13 - Hangi yılın toplam "runtime" süresi en fazladır?
    def question13():
        PreRun = data.iloc[:,2:4]
        PreRun["Premiere"] = pd.to_datetime(PreRun["Premiere"]) 
        PreRun['Premiere'] = PreRun['Premiere'].dt.strftime('%Y')
        PreRun = PreRun.groupby(["Premiere"]).sum()
        PreRun = PreRun.sort_values(ascending=False,by=["Runtime"])
        colors2 = ['lightslategray',] * 8
        colors2[0] = "crimson"
        PreRun.plot(kind='pie', x="Premiere", y="Runtime", autopct='%1.0f%%',explode=[0.2,0,0,0,0,0,0,0], colors=colors2)
        plt.legend(loc="upper left")
    
        plt.axis("equal")
        plt.tight_layout()
        plt.show()

    # Q14 - Her bir dilin en fazla kullanıldığı "Genre" nedir?
    def question14():
        LanGenre = data.groupby(["Language"])
        l2 = LanGenre[["Genre"]].describe()
        l2 = l2[("Genre" , "top")]
        print(l2)

    # Q15 - Veri setinde outlier veri var mıdır? Açıklayınız.
    def question15():
        
        answer = "With the box plot graph, 82 outliers were determined in the data and removed from the data set. In this way, the number of data, which was 584 at the beginning, decreased to 502. The visualizations were made on 502 data."
        plt.xlabel("Runtime")
        plt.boxplot(data["Runtime"])
        plt.show()

        plt.boxplot(data["IMDB Score"])
        plt.xlabel("IMDB Score")
        plt.show()

#To continue the loop
p1 = True
# Using input values for getting answer of questions
while p1 == True:
    try:
        process = input('\033[95m'+"Enter the question number whose answer you want to show...\n" + '\033[0m')
        numberInput(process)
        notinList(process)
    except notinListError:
        print('\033[93m'+f"Please just enter numbers in the list!({questions_list[0]} - {questions_list[-1]})\n----------------------------------------\n" + '\033[0m')
        p1 = True

    except numberInputError:
        print('\033[93m'+"Please just enter numbers !!\n-------------------\n"+'\033[0m')
        p1 = True
    else:
        p1 = False

p2 = True
while p2==True: 
    if process == "1":
        questions.question1()
    elif process == "2":
        questions.question2()
    elif process == "3":
        questions.question3()
    elif process == "4":
        questions.question4()
    elif process == "5":
        questions.question5()
    elif process == "6":
        questions.question6()
    elif process == "7":
        questions.question7()
    elif process == "8":
        questions.question8()
    elif process == "9":
        questions.question9()
    elif process == "10":
        questions.question10()
    elif process == "11":
        questions.question11()
    elif process == "12":
        questions.question12()
    elif process == "13":
        questions.question13()
    elif process == "14":
        questions.question14()
    elif process == "15":
        questions.question15()
    try:
        process = input('\033[95m'+"Enter the question number whose answer you want to show...\n(or Please write \"E or e\" to close the program)" + '\033[0m \n')
        exitPass(process)
        numberInput(process)
        notinList(process)
        
        
    except notinListError:
        print('\033[93m' + f"-----------------------------------------------\nPlease just enter numbers in the list!({questions_list[0]} - {questions_list[-1]})\n-----------------------------------------------\n" + '\033[0m') 
        p2 = True
    except exitPassError:
        print("Exiting the program...")
        time.sleep(2)
        break
    except numberInputError:
        print('\033[93m'+"------------------------------\nPlease just enter numbers !!\n------------------------------\n"+'\033[0m')
        p2 = True
    else:
        p2 = True
    
        
 

