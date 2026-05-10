import instaloader

    L = instaloader.Instaloader(
        download_videos=True,
        download_video_thumbnails=True,
        download_pictures=True
)

# Login

    try:
        L.login("inserisciiltuonomequi", "inseriscilatuapasswordqui")
        print("Loggato con successo!")
    except Exception as e:
        print(f"Login fallito: {e}")
        print("Continuo senza login...")


    L.context.sleep = True 
    sanitize_paths=True

    shortcode = input();   # messo solo per prendere piu' link alla volta,
                       # basta mettere uno spazio tra l'uno e l'altro
    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target="downloads")
        print("Download eseguito con successo!")
    except Exception as e:
        print(f"Errore: {e}") # letteralmente la stampa dell'errore