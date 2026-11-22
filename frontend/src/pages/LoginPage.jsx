import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import api from '../api/axios'

function LoginPage() {
  const [isRegister, setIsRegister] = useState(false)
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)

    try {
      let response

      if (isRegister) {
        response = await api.post('/api/auth/register', { email, password })
      } else {
        const formData = new URLSearchParams()
        formData.append('username', email)
        formData.append('password', password)

        response = await api.post('/api/auth/login', formData, {
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        })
      }

      localStorage.setItem('access_token', response.data.access_token)
      navigate('/', { replace: true })
    } catch (err) {
      setError(err.response?.data?.detail || 'Ошибка авторизации. Проверьте данные.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <main style={{ maxWidth: '360px', margin: '60px auto', padding: '0 16px' }}>
      <h1>{isRegister ? 'Регистрация' : 'Вход'}</h1>

      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Пароль"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        {error && <p style={{ color: 'red', margin: 0 }}>{error}</p>}

        <button type="submit" disabled={loading}>
          {loading ? 'Загрузка...' : isRegister ? 'Зарегистрироваться' : 'Войти'}
        </button>
      </form>

      <button
        type="button"
        onClick={() => {
          setIsRegister(!isRegister)
          setError('')
        }}
        style={{ marginTop: '12px', background: 'none', border: 'none', cursor: 'pointer', textDecoration: 'underline' }}
      >
        {isRegister ? 'Уже есть аккаунт? Войти' : 'Нет аккаунта? Зарегистрироваться'}
      </button>
    </main>
  )
}

export default LoginPage