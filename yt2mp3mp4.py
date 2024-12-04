import os
import yt_dlp

def download_mp3(youtube_links, output_dir="downloads"):
    """
    Downloads MP3 files from YouTube links without using FFmpeg.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"[INFO] Created output directory: {output_dir}")

    ydl_opts = {
        'format': 'bestaudio/best',  # Download the best audio quality available
        'extractaudio': True,       # Extract audio
        'audioformat': 'mp3',       # Save directly in MP3 format
        'postprocessor_args': ['-vn'],  # Skip video (if applicable)
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    }

    for link in youtube_links:
        try:
            print(f"\n[DEBUG] Processing link: {link}")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            print(f"\n[INFO] Successfully downloaded: {link}")
        except Exception as e:
            print(f"\n[ERROR] Failed to process {link}. Error: {e}\n")

def download_mp4(youtube_links, output_dir="videos"):
    """
    Downloads MP4 videos in 1080p60fps quality without requiring FFmpeg.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"[INFO] Created output directory: {output_dir}")

    ydl_opts = {
        'format': 'bestvideo[height=1080][fps=60]+bestaudio/best',  # Best video and audio matching 1080p60fps
        'merge_output_format': 'mp4',                              # Output file format as MP4
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Output file name with YouTube title
    }

    for link in youtube_links:
        try:
            print(f"[DEBUG] Processing link: {link}")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            print(f"[INFO] Successfully downloaded: {link}")
        except Exception as e:
            print(f"[ERROR] Failed to process {link}. Error: {e}")


if __name__ == "__main__":
    # youtube_mp3_links = [
    #     "https://www.youtube.com/watch?v=CQlFt_TI1XE",
    #     "https://www.youtube.com/watch?v=hqNqcPh4MWY",
    #     "https://www.youtube.com/watch?v=npt9Nffuu3k",
    #     "https://www.youtube.com/watch?v=alIjIBHJVhc"
    # ]
    # print("[INFO] Starting MP3 download script")
    # download_mp3(youtube_mp3_links)
    # print("\n[INFO] Script finished")

    youtube_mp4_links = [
        "https://www.youtube.com/watch?v=DlRO_5HBAHg"
    ]
    print("[INFO] Starting MP4 download script")
    download_mp4(youtube_mp4_links)
    print("\n[INFO] Script finished")
