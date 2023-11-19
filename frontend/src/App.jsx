import { useEffect, useState } from 'react'
import axios from 'axios'

const App = () => {
  const [selectedFile, setSelectedFile] = useState(null)
  const [result, setResult] = useState('')

  const baseUrl = import.meta.env.VITE_BASE_URL
    ? import.meta.env.VITE_BASE_URL
    : 'http://localhost:5000'

  useEffect(() => {
    axios.get(baseUrl)
      .then((response) => {
        console.log(baseUrl)
        console.log(response.data)
      })
  }, [baseUrl])

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0])
  }

  const handleSubmit = async () => {
    if (!selectedFile) {
      alert('Please select a file before submitting.')
      return
    }

    // https://developer.mozilla.org/en-US/docs/Web/API/FormData
    const formData = new FormData()
    formData.append('file', selectedFile)

    try {
      const response = await axios.post(baseUrl, formData)
      console.log(response.data)
      setResult(response.data.prediction)
    } catch (error) {
      console.error('Error uploading file:', error)
    }
  }

  return (
    <>
      <h1>Image Number Prediction</h1>

      <div>
        <input type="file" onChange={handleFileChange} />
      </div>

      <div>
        <button onClick={handleSubmit}>Predict</button>
      </div>

      <div>
        <p>Result: {result}</p>
      </div>

    </>
  )
}

export default App
