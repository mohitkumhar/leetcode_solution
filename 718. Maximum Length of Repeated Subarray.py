# class Solution(object):
#     def findLength(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: int
#         """

#         check_list = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
#         max_length = 0

#         for i in range(1, len(nums1) + 1):
#             for j in range(1, len(nums2) + 1):

#                 if nums1[i - 1] == nums2[j - 1]:
#                     check_list[i][j] = check_list[i - 1][j - 1] + 1
#                     max_length = max(max_length, check_list[i][j])

#         return max_length
import youtube_dl

def get_playlist_titles(playlist_url):
    ydl_opts = {
        'quiet': True,  # Suppress console output
        'extract_flat': True,  # Extract only the playlist items, not the whole hierarchy
        'force_generic_extractor': True,  # Use generic extractor for playlists, bypassing potential issues with specific extractors
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)

    if 'entries' in playlist_info:
        return [video['title'] for video in playlist_info['entries']]
    else:
        return []

playlist_url = input("Enter the URL of the YouTube playlist: ")
titles = get_playlist_titles(playlist_url)

print("Titles of videos in the playlist:")
for title in titles:
    print(title)
