# -*- coding: utf-8 -*-
import scrapy
import re
import json

from scrapy.loader import ItemLoader
from ..items import TopnpiItem


class TopnpiReviewSpider(scrapy.Spider):
    name = 'topnpi_review'
    allowed_domains = ['topnpi.com']
    start_urls = [
        'https://www.topnpi.com/oh1982660171/dr-stephen-guy',
        'https://www.topnpi.com/oh1639118284/dr-mickey-denen',
        'https://www.topnpi.com/oh1891741872/dr-warren-ljungren',
        'https://www.topnpi.com/oh1508980202/dr-michelle-degroat',
        'https://www.topnpi.com/oh1093793762/dr-david-mesker',
        'https://www.topnpi.com/oh1902845001/dr-sally-mcintyre',
        'https://www.topnpi.com/oh1073552782/dr-louis-heckman',
        'https://www.topnpi.com/oh1356396766/dr-chethana-raghupathy',
        'https://www.topnpi.com/oh1174562888/dr-ronald-pohlman',
        'https://www.topnpi.com/oh1710932975/dr-angela-kohnen',
        'https://www.topnpi.com/oh1497700678/dr-mark-ringle',
        'https://www.topnpi.com/oh1649219874/dr-gary-conley',
        'https://www.topnpi.com/oh1265487250/dr-terez-metry',
        'https://www.topnpi.com/oh1346287091/dr-salva-ahmed',
        'https://www.topnpi.com/oh1912992165/dr-susan-davis-brown',
        'https://www.topnpi.com/oh1295722635/dr-heidi-buckingham',
        'https://www.topnpi.com/oh1346622578/dr-michelle-nissen',
        'https://www.topnpi.com/oh1700179744/dr-spencer-wolf',
        'https://www.topnpi.com/oh1255386744/dr-miguel-parilo',
        'https://www.topnpi.com/oh1679695985/dr-trisha-zeidan',
        'https://www.topnpi.com/oh1881633386/dr-paul-brammer',
        'https://www.topnpi.com/oh1033326467/dr-nicholas-davis',
        'https://www.topnpi.com/oh1588618714/dr-melinda-ruff',
        'https://www.topnpi.com/oh1093793762/dr-david-mesker',
        'https://www.topnpi.com/oh1811943822/dr-ravindra-mullapudi',
        'https://www.topnpi.com/oh1578559449/dr-aaron-harju',
        'https://www.topnpi.com/oh1285601765/dr-anupama-kulkarni',
        'https://www.topnpi.com/oh1760484315/dr-patrick-larreategui',
        'https://www.topnpi.com/oh1720080344/dr-lyle-lowry',
        'https://www.topnpi.com/oh1851366553/dr-daniel-taylor',
        'https://www.topnpi.com/oh1003883646/dr-daniel-elshoff',
        'https://www.topnpi.com/oh1538136577/dr-robert-klamar',
        'https://www.topnpi.com/oh1366419350/dr-tammy-taylor',
        'https://www.topnpi.com/oh1942278940/dr-paul-weber',
        'https://www.topnpi.com/oh1780899633/dr-geetha-ambalavanan',
        'https://www.topnpi.com/oh1174563282/dr-anjana-shah',
        'https://www.topnpi.com/oh1891759668/dr-patricia-grice',
        'https://www.topnpi.com/oh1710941513/dr-robert-harrington',
        'https://www.topnpi.com/oh1952516544/dr-joseph-allen',
        'https://www.topnpi.com/oh1316942063/dr-christopher-lauricella',
        'https://www.topnpi.com/oh1245287911/dr-james-aldstadt',
        'https://www.topnpi.com/oh1407896061/dr-ronald-mcgilton',
        'https://www.topnpi.com/oh1376590091/dr-polina-sadikov',
        'https://www.topnpi.com/oh1376533463/dr-james-decaestecker/oh-1',
        'https://www.topnpi.com/oh1023064433/dr-annadorai-kalahasthy',
        'https://www.topnpi.com/oh1861431512/dr-julie-myers',
        'https://www.topnpi.com/oh1215976428/dr-thomas-brunsman',
        'https://www.topnpi.com/oh1225026479/dr-marcus-washington',
        'https://www.topnpi.com/oh1720277486/dr-jon-silk',
        'https://www.topnpi.com/oh1528007754/dr-kevin-sharrett',
        'https://www.topnpi.com/oh1851671457/dr-neva-dehart',
        'https://www.topnpi.com/oh1811936404/dr-theodore-garland',
        'https://www.topnpi.com/oh1487694642/dr-chester-robinson/oh-1',
        'https://www.topnpi.com/oh1265410203/dr-scot-denmark',
        'https://www.topnpi.com/oh1801875877/dr-john-miller',
        'https://www.topnpi.com/oh1144315086/dr-james-gilchrist',
        'https://www.topnpi.com/oh1205921061/dr-bruce-ladle',
        'https://www.topnpi.com/oh1942229364/dr-laszlo-toth',
        'https://www.topnpi.com/oh1255463048/dr-kimberly-diltz',
        'https://www.topnpi.com/oh1871559179/dr-lisa-mix',
        'https://www.topnpi.com/oh1386623817/dr-keith-watson',
        'https://www.topnpi.com/oh1114148376/dr-irina-gendler',
        'https://www.topnpi.com/oh1982671434/dr-roger-goodenough',
        'https://www.topnpi.com/oh1134137540/dr-richard-michael',
        'https://www.topnpi.com/oh1700274347/dr-young-un-kim',
        'https://www.topnpi.com/oh1982607172/dr-cass-cullis',
        'https://www.topnpi.com/oh1629071808/dr-william-czajka',
        'https://www.topnpi.com/oh1396837985/dr-aaron-kaibas',
        'https://www.topnpi.com/oh1881696060/dr-sameh-khouzam',
        'https://www.topnpi.com/oh1609872027/dr-don-delcamp',
        'https://www.topnpi.com/oh1104077064/dr-mark-zunkiewicz',
        'https://www.topnpi.com/oh1013992783/dr-jon-sulentic',
        'https://www.topnpi.com/oh1821073230/dr-jerry-magone',
        'https://www.topnpi.com/oh1427161975/dr-erika-penrod',
        'https://www.topnpi.com/oh1770568065/dr-anthony-checroun',
        'https://www.topnpi.com/oh1982718813/dr-scott-albright',
        'https://www.topnpi.com/oh1326019613/dr-jeffery-adam',
        'https://www.topnpi.com/oh1922236447/dr-ristenka-prnarova',
        'https://www.topnpi.com/oh1518123082/dr-mohammed-ahmed',
        'https://www.topnpi.com/oh1356427223/dr-anessa-alappatt',
        'https://www.topnpi.com/oh1174799118/dr-michele-carlson',
        'https://www.topnpi.com/oh1699777623/dr-bhadresh-doshi',
        'https://www.topnpi.com/oh1437235058/dr-sharon-carpenter',
        'https://www.topnpi.com/oh1932181849/dr-mark-friedman',
        'https://www.topnpi.com/oh1104847516/dr-deitrice-chapman/oh-1',
        'https://www.topnpi.com/oh1437198579/dr-joseph-garland',
        'https://www.topnpi.com/oh1902899966/dr-larry-holland',
        'https://www.topnpi.com/tx1225005358/dr-brandon-horne/oh-1',
        'https://www.topnpi.com/oh1841494416/dr-amina-husain',
        'https://www.topnpi.com/oh1336136670/dr-brent-imbody',
        'https://www.topnpi.com/oh1104882976/dr-bradley-jacobs',
        'https://www.topnpi.com/oh1790032118/dr-cassandra-milling',
        'https://www.topnpi.com/oh1922003722/dr-shelly-joiner',
        'https://www.topnpi.com/oh1487643623/dr-leesa-kaufman',
        'https://www.topnpi.com/oh1194863563/dr-ahmed-fathy',
        'https://www.topnpi.com/oh1891781910/dr-charles-hall',
        'https://www.topnpi.com/oh1235197807/dr-rajan-krishnamani',
        'https://www.topnpi.com/oh1619967650/dr-luan-tran/oh-1',
        'https://www.topnpi.com/oh1033111232/dr-sudhakar-maraboyina',
        'https://www.topnpi.com/ny1366769796/dr-joseph-fasanello',
        'https://www.topnpi.com/tn1770857484/dr-carlo-buena']


# https://www.topnpi.com/sc1538455829/dr-merri-paden
# https://www.topnpi.com/sc1689110215/dr-danielle-motley-jennings
# https://www.topnpi.com/sc1538455829/dr-merri-paden

    def parse(self, response):
        JSObject = response.css(
            'script[type="application/ld+json"]::text').extract_first()
        if JSObject and len(JSObject) > 0:
            jsonObject = json.loads(JSObject)
            try:
                nodes = jsonObject[2]
                try:
                    name = nodes['name']
                except:
                    name = 'NA'
                try:
                    category = nodes['@type']
                except:
                    category = 'NA'
                try:
                    description = nodes['description']
                except:
                    description = 'NA'
                try:
                    hospitalAffiliation = nodes['hospitalAffiliation']['name']
                except:
                    hospitalAffiliation = 'NA'
                try:
                    email = nodes['email']
                    if email == '':
                        email = 'NA'
                except:
                    email = 'NA'
                try:
                    telephone = nodes['telephone']
                except:
                    telephone = 'NA'
                try:
                    url = nodes['url']
                except:
                    url = 'NA'

            except:
                print('No Information is available')

            try:
                nodesReview = jsonObject[2]['review']
                for node in nodesReview:
                    reviewer_name = node['author']
                    recommend = node['name']
                    review_date = node['datePublished']
                    reviews = node['description']
                    review = reviews.replace(';', '.')

                    print("\n Review: ", review, "\n\n")
                    l = ItemLoader(item=TopnpiItem())

                    l.add_value('name', name)
                    l.add_value('category', category)
                    l.add_value('description', description)
                    l.add_value('hospitalAffiliation', hospitalAffiliation)
                    l.add_value('email', email)
                    l.add_value('telephone', telephone)
                    l.add_value('reviewer_name', reviewer_name)
                    l.add_value('recommend', recommend)
                    l.add_value('review_date', review_date)
                    l.add_value('review', review)
                    l.add_value('url', url)

                    yield(l.load_item())
                # return self.pasingProcess(
                #     name, category, description, hospitalAffiliation, email, telephone, reviewer_name, recommend, review_date, review, url)

            except:
                print("!!No Review is available!!")

                l = ItemLoader(item=TopnpiItem())

                l.add_value('name', name)
                l.add_value('category', category)
                l.add_value('description', description)
                l.add_value('hospitalAffiliation', hospitalAffiliation)
                l.add_value('email', email)
                l.add_value('telephone', telephone)
                l.add_value('reviewer_name', 'NA')
                l.add_value('recommend', 'NA')
                l.add_value('review_date', 'NA')
                l.add_value('review', 'NA')
                l.add_value('url', url)

                yield(l.load_item())
    #             return self.pasingProcess(
    #                 name, category, description, hospitalAffiliation, email, telephone, '', '', '', '', url)
    #
    # def pasingProcess(self, name, category, description, hospitalAffiliation, email, telephone, reviewer_name, recommend, review_date, review, url):
    #
    #     l = ItemLoader(item=TopnpiItem())
    #
    #     l.add_value('name', name)
    #     l.add_value('category', category)
    #     l.add_value('description', description)
    #     l.add_value('hospitalAffiliation', hospitalAffiliation)
    #     l.add_value('email', email)
    #     l.add_value('telephone', telephone)
    #     l.add_value('reviewer_name', reviewer_name)
    #     l.add_value('recommend', recommend)
    #     l.add_value('review_date', review_date)
    #     l.add_value('review', review)
    #     l.add_value('url', url)
    #
    #     print("\n\n", l.load_item(), "\n\n")
    #
    #     return l.load_item()
