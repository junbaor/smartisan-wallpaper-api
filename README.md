# smartisan-wallpaper-api

### 请求
> 查询所有来源  

`http://api-app.smartisan.com/app/index.php?r=paperapi/index/list&client_version=2&limit=20&paper_id=0`

> 查询 Pexels 来源  

`http://api-app.smartisan.com/app/index.php?r=paperapi/index/list&client_version=2&source=Pexels&limit=20&paper_id=0`

* `limit` 每页条数
* `paper_id` 开始 id , 即响应中的 id
* `source` 来源

### 来源可选值
* Artand
* Unsplash
* Minimography
* Pexels
* Magdeleine
* Fancycrave
* Snapwiresnaps
* Memento
* 壁纸摄影大赛精选


### 响应实例
```
{
    "code":0,
    "data":[
        {
            "id":"32656",
            "title":"",
            "author":"Osman Rana",
            "url":"http://image.smartisanos.cn/papers/unsplash/533F0B95DBD1B5023D3C2B7B11021175.jpg",
            "created_time":"1498549856",
            "source":"Unsplash",
            "width":"2185",
            "height":"3059",
            "desc":"",
            "sour_url":"",
            "publiced_time":"1498549856"
        }
    ],
    errInfo":[

    ]
}
```
