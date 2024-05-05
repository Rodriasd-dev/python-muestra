//Estas películas son las que tienen un rating de 8.5 para arriba
const datos_json = [
            {'anime_id': 32281, 'name': 'Kimi no Na wa.', 'genre': 'Drama, Romance, School, Supernatural', 'type': 'Movie', 'episodes': '1', 'rating': 9.37, 'members': 200630}, 
            {'anime_id': 15335, 'name': 'Gintama Movie: Kanketsu-hen - Yorozuya yo Eien Nare', 'genre': 'Action, Comedy, Historical, Parody, Samurai, Sci-Fi, Shounen', 'type': 'Movie', 'episodes': '1', 'rating': 9.1, 'members': 72534}, 
            {'anime_id': 28851, 'name': 'Koe no Katachi', 'genre': 'Drama, School, Shounen', 'type': 'Movie', 'episodes': '1', 'rating': 9.05, 'members': 102733}, 
            {'anime_id': 199, 'name': 'Sen to Chihiro no Kamikakushi', 'genre': 'Adventure, Drama, Supernatural', 'type': 'Movie', 'episodes': '1', 'rating': 8.93, 'members': 466254}, 
            {'anime_id': 12355, 'name': 'Ookami Kodomo no Ame to Yuki', 'genre': 'Fantasy, Slice of Life', 'type': 'Movie', 'episodes': '1', 'rating': 8.84, 'members': 226193}, 
            {'anime_id': 164, 'name': 'Mononoke Hime', 'genre': 'Action, Adventure, Fantasy', 'type': 'Movie', 'episodes': '1', 'rating': 8.81, 'members': 339556}, 
            {'anime_id': 7311, 'name': 'Suzumiya Haruhi no Shoushitsu', 'genre': 'Comedy, Mystery, Romance, School, Sci-Fi, Supernatural', 'type': 'Movie', 'episodes': '1', 'rating': 8.81, 'members': 240297}, 
            {'anime_id': 28957, 'name': 'Mushishi Zoku Shou: Suzu no Shizuku', 'genre': 'Adventure, Fantadsy, Historical, Mystery, Seinen, Slice of Life, Supernatural', 'type': 'Movie', 'episodes': '1', 'rating': 8.75, 'members': 32266}, 
            {'anime_id': 431, 'name': 'Howl no Ugoku Shiro', 'genre': 'Adventure, Drama, Fantasy, Romance', 'type': 'Movie', 'episodes': '1', 'rating': 8.74, 'members': 333186}, 
            {'anime_id': 31757, 'name': 'Kizumonogatari II: Nekketsu-hen', 'genre': 'Action, Mystery, Supernatural, Vampire', 'type': 'Movie', 'episodes': '1', 'rating': 8.73, 'members': 34347}, 
            {'anime_id': 4282, 'name': 'Kara no Kyoukai 5: Mujun Rasen', 'genre': 'Action, Drama, Mystery, Romance, Supernatural, Thriller', 'type': 'Movie', 'episodes': '1', 'rating': 8.68, 'members': 111074}, 
            {'anime_id': 4565, 'name': 'Tengen Toppa Gurren Lagann Movie: Lagann-hen', 'genre': 'Action, Mecha, Sci-Fi, Space, Super Power', 'type': 'Movie', 'episodes': '1', 'rating': 8.64, 'members': 82253}, 
            {'anime_id': 11577, 'name': 'Steins;Gate Movie: Fuka Ryouiki no D�j� vu', 'genre': 'Sci-Fi, Thriller', 'type': 'Movie', 'episodes': '1', 'rating': 8.61, 'members': 192424}, 
            {'anime_id': 10408, 'name': 'Hotarubi no Mori e', 'genre': 'Drama, Romance, Shoujo, Supernatural', 'type': 'Movie', 'episodes': '1', 'rating': 8.61, 'members': 197439}, 
            {'anime_id': 21899, 'name': 'Gintama: Yorinuki Gintama-san on Theater 2D', 'genre': 'Action, Comedy, Historical, Parody, Samurai, Sci-Fi, Shounen', 'type': 'Movie', 'episodes': '2', 'rating': 8.6, 'members': 11104}, 
            {'anime_id': 7472, 'name': 'Gintama Movie: Shinyaku Benizakura-hen', 'genre': 'Action, Comedy, Historical, Parody, Samurai, Sci-Fi, Shounen', 'type': 'Movie', 'episodes': '1', 'rating': 8.59, 'members': 51185}, 
            {'anime_id': 28805, 'name': 'Bakemono no Ko', 'genre': 'Adventure, Supernatural', 'type': 'Movie', 'episodes': '1', 'rating': 8.58, 'members': 80825}, 
            {'anime_id': 578, 'name': 'Hotaru no Haka', 'genre': 'Drama, Historical', 'type': 'Movie', 'episodes': '1', 'rating': 8.58, 'members': 174878}, 
            {'anime_id': 5205, 'name': 'Kara no Kyoukai 7: Satsujin Kousatsu (Kou)', 'genre': 'Action, Mystery, Romance, Supernatural, Thriller', 'type': 'Movie', 'episodes': '1', 'rating': 8.57, 'members': 95658}, 
            {'anime_id': 18617, 'name': 'Girls und Panzer der Film', 'genre': 'Military, School', 'type': 'Movie', 'episodes': '1', 'rating': 8.55, 'members': 25641}, 
            {'anime_id': 30346, 'name': 'Doukyuusei (Movie)', 'genre': 'Romance, School, Shounen Ai, Slice of Life', 'type': 'Movie', 'episodes': '1', 'rating': 8.53, 'members': 28864}, 
            {'anime_id': 3784, 'name': 'Evangelion: 2.0 You Can (Not) Advance', 'genre': 'Action, Mecha, Sci-Fi', 'type': 'Movie', 'episodes': '1', 'rating': 8.53, 'members': 182224}, 
            {'anime_id': 33607, 'name': 'Kahei no Umi', 'genre': 'Historical', 'type': 'Movie', 'episodes': '1', 'rating': 9.33, 'members': 44}, 
            {'anime_id': 25301, 'name': 'Maya no Isshou', 'genre': 'Drama, Historical, Slice of Life', 'type': 'Movie', 'episodes': '1', 'rating': 8.75, 'members': 66}, 
            {'anime_id': 33980, 'name': 'Mirai ni Mukete: Bousai wo Kangaeru', 'genre': 'Drama', 'type': 'Movie', 'episodes': '1', 'rating': 9.0, 'members': 77}, 
            {'anime_id': 23005, 'name': 'Mogura no Motoro', 'genre': 'Slice of Life', 'type': 'Movie', 'episodes': '1', 'rating': 9.5, 'members': 62}, 
            {'anime_id': 26145, 'name': 'Okaachan Gomen ne', 'genre': 'Historical, Kids', 'type': 'Movie', 'episodes': '1', 'rating': 9.0, 'members': 47}, 
            {'anime_id': 32627, 'name': 'Shaka no Shougai', 'genre': 'Historical', 'type': 'Movie', 'episodes': '1', 'rating': 9.0, 'members': 31}, 
            {'anime_id': 32796, 'name': 'Shenmi Shijie Lixian Ji', 'genre': 'Adventure, Comedy, Fantasy', 'type': 'Movie', 'episodes': '1', 'rating': 9.0, 'members': 37}, 
            {'anime_id': 22995, 'name': 'Shisei Sasshin', 'genre': 'Slice of Life', 'type': 'Movie', 'episodes': '1', 'rating': 8.67, 'members': 51}, 
            {'anime_id': 33662, 'name': 'Taka no Tsume 8: Yoshida-kun no X-Files', 'genre': 'Comedy, Parody', 'type': 'Movie', 'episodes': '1', 'rating': 10.0, 'members': 13}
            ]