// Импортируем необходимые библиотеки
import React, { useState, useEffect } from 'react';
import axios from 'axios';

// Создаем компонент User, который отображает информацию об одном пользователе
const User = ({ user }) => {
  // Используем деструктуризацию, чтобы получить свойства объекта user
  const { image_url, name, age, gender, interest, specialization } = user;

  // Возвращаем JSX-элемент, который содержит информацию о пользователе
  return (
    <div className="user">
      <img src={image_url} alt={name} className="user-image" />
      <div className="user-info">
        <h3 className="user-name">{name}</h3>
        <p className="user-age">Возраст: {age}</p>
        <p className="user-gender">Пол: {gender === 'M' ? 'Мужчина' : 'Женщина'}</p>
        <p className="user-interest">Интересы: {interest.map(i => i.name).join(', ')}</p>
        <p className="user-specialization">Специализация: {specialization.name}</p>
      </div>
    </div>
  );
};

// Создаем компонент Users, который отображает список всех пользователей
const App = () => {
  // Создаем состояние для хранения списка пользователей
  const [users, setUsers] = useState([]);

  // Используем эффект, чтобы получить данные с сервера Django при монтировании компонента
  useEffect(() => {
    // Создаем функцию, которая делает запрос с помощью axios
    const fetchUsers = async () => {
      // Пытаемся получить данные с сервера
      try {
        // Определяем адрес сервера Django
        const djangoUrl = 'http://localhost:8000';
        // Делаем GET-запрос к эндпоинту /users, который возвращает список пользователей в формате JSON
        const response = await axios.get(`${djangoUrl}/users/`);
        // Получаем данные из ответа
        const data = response.data;
        // Обновляем состояние с помощью полученных данных
        setUsers(data);
      } catch (error) {
        // Выводим ошибку в консоль, если запрос не удался
        console.error(error);
      }
    };

    // Вызываем функцию, которая делает запрос
    fetchUsers();
  }, []); // Передаем пустой массив в качестве зависимости, чтобы эффект сработал только один раз при монтировании

  // Возвращаем JSX-элемент, который содержит список пользователей
  return (
    <div className="users">
      <h1 className="users-title">Пользователи</h1>
      <div className="users-list">
        {users.map(user => (
          // Добавляем атрибут key, используя id или имя пользователя
          <User key={user.id} user={user} />
          // <User key={user.name} user={user} />
        ))}
      </div>
    </div>
  );
};

// Экспортируем компонент Users
export default App;
