from functools import reduce

animal_list = [
    { "type" : "monkey", "emoji": "🐒", "name":"Chita" , "diet": "herbivorous" },
    { "type" : "raccoon", "emoji": "🦝", "name": "RJ" , "diet": "omnivore"  },
    { "type" : "fox", "emoji": "🦊" , "name": "Jony" ,  "diet" : "carnivorous" },
    { "type" : "wolf", "emoji": "🐺" , "name": "Jacob" , "diet" : "carnivorous" },
    { "type" : "tiger", "emoji": "🐅" , "name":"Toño"   ,"diet" : "carnivorous" },
    { "type" : "unicorn", "emoji": "🦄",  "name":"Magic", "diet": "herbivorous"  }
]



{
    "herbivorous" : {
        "total" : 2,
        "animals": [ ('🐒',"monkey" ,"Chita"), ('🦄',"unicorn" , "Magic")  ]
    },
    "omnivore" :  {
        "total" : 1,
        "animals": [ ('🦝',"raccoon" ,"RJ") ]
    },
    "carnivorous" : {
        "total" : 3,
        "animals": [ ('🦊',"fox" ,"Jony"), ('🐺',"wolf" ,"Jacob"), ('🐅',"tiger" ,"Toño") ]
    } 
}
