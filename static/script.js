const uploaded_img = document.getElementById('img-upload')
const image_name = document.getElementById('img-name')
const image_size = document.getElementById('img-size')
const preview = document.getElementById("upload-img")


// listner for file upload
uploaded_img.addEventListener('change', fileUpload)

function fileUpload(event) {
    const file = event.target.files[0]

    if (file) {
        const fileName = file.name
        const fileSize = file.size

        // file size from bytes to KB
        const fileSizeKB = (fileSize / 1024).toFixed(2)

        document.body.style.backgroundColor = "#b0c8e8"

        image_name.textContent = `Image Name: ${fileName}`
        image_size.textContent = `Image Size: ${fileSizeKB} KB`


        // listner for image preview
        const reader = new FileReader()
        reader.addEventListener('load', function (e) {
            preview.setAttribute('src', e.target.result);
            preview.style.display = 'block';
        }
    )
        reader.readAsDataURL(file)
    }

    else {
        image_name.textContent = 'File not selected'
        image_size.textContent = 'File not selected'
    }
}
