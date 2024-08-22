## MAGICK: A Large-scale Captioned Dataset Matting Generated Images using Chroma Keying
Ryan D Burgert, Brian L. Price, Jason Kuen, Yijun Li, Michael S Ryoo

Presented at CVPR 2024, the MAGICK dataset is a comprehensive collection of over 140,000 high-quality, captioned, single-subject 1024x1024 RGBA images. It is large enough to be used for image generation tasks!

### Resources
- **Project Website:** [ryanndagreat.github.io/MAGICK](https://ryanndagreat.github.io/MAGICK)
- **Paper:** [Read it here!](https://drive.google.com/file/d/1Eec6MQZOy00Qwgy1gvWHVSCfnuUqOwKz/view?usp=sharing)

### Dataset Explorer
Explore the dataset using our custom-built explorer: [MAGICK Dataset Explorer](https://ryanndagreat.github.io/MAGICK/Explorer/magick_rgba_explorer.html)

### Using the Dataset
To use this dataset, download the index file and utilize the `page_id` and `subject` columns for data handling. `subject` provides the text caption for each image. Convert a `page_id` to its corresponding image URL using the following Python function:

```python
def page_id_to_url(page_id):
    return f"https://huggingface.co/datasets/OneOverZero/MAGICK/resolve/main/images/{page_id[:2]}/{page_id}.png"
```

### Download
- **Index File:** [MAGICK Index (TSV Format)](https://huggingface.co/datasets/OneOverZero/MAGICK/resolve/main/magick_index.tsv)
- Of course, you can also git clone the hugginface repository via `git clone https://huggingface.co/datasets/OneOverZero/MAGICK` to download the whole thing in one go. Its approximately 200GB.

![CVPR2024 Poster](poster.png)
