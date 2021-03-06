def find_key(var):
    if var == 'ALGORITHMS':
        return 'RS256'
    elif var == 'API_AUDIENCE':
        return 'movie_project'
    elif var == 'AUTH0_DOMAIN':
        return 'fsnd-coffee-project.auth0.com'
    elif var == 'DATABASE_URL':
        return 'postgres://lmbzhqhvtomrqy:14f12f71b9fa248ede5e56eee5e07d9e206c46c66c1d89b6ac4f09d9bbbc1421@ec2-52-71-55-81.compute-1.amazonaws.com:5432/dbrvtudjr80g1g'
    elif var == 'EXCITED':
        return 'true'
    elif var == 'casting_assistant':
        return 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkFEMVZrLU5pVkFvSmRvNmlOVnU1WCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY29mZmVlLXByb2plY3QuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEwOTQyODg3MTQzMzk4NDkxMzU0IiwiYXVkIjoibW92aWVfcHJvamVjdCIsImlhdCI6MTU4ODk1ODA0NywiZXhwIjoxNTg5MDQ0NDQ3LCJhenAiOiJBSEZwdXM5cmthZHJwU2lXaXpLS3FCZWw2TE9maHJNOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.w6kWFXHMzvUSYpNdeYSqf5eFrZ2OWSQlrLqkNFFzgp1F-IaQCaMA50uO6l6mNUlcMv8d7D5Y3JMaT0p1b26fKMgzxd4CIz8yYU5mEarYtbl3gzUmBNouAovkE30h7eKWW44jvO5c9QHC9tLQZfOwkEu1jC7kb7Rk1oBrZQv0R3qCjtyEGhSVgs9OBsU9dJHNPEfcG8-JYi6ngY2dvfy_pi_k4Yj5X4s0Esin6FQSp9J8zpB8TlDkEWu_Pp53q0K3NI4OmNs3uJZhT4UbkoqynBz8ydz1co9abOu0v0Lo-dl6N4luy2F0ukXHuPeOCCezhfcUI-waMDsKDtNnWzXq0g'
    elif var == 'casting_director':
        return 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkFEMVZrLU5pVkFvSmRvNmlOVnU1WCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY29mZmVlLXByb2plY3QuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEwOTQyODg3MTQzMzk4NDkxMzU0IiwiYXVkIjoibW92aWVfcHJvamVjdCIsImlhdCI6MTU4ODk1Nzk0MiwiZXhwIjoxNTg5MDQ0MzQyLCJhenAiOiJBSEZwdXM5cmthZHJwU2lXaXpLS3FCZWw2TE9maHJNOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.VmaWWM0nipmSRhzEJSnkQJMOxnLfvz-IPONheOTzkRlIKxSawpaNYYHVPtOePiCAWAFI6GaFIUhp6fo9n_S50g3xCHDraqnAj3fPL5jWQN5wWPctkm40SDMHVZzaxzLNccy9kKKgjdF08dB6fpkFVJvsRjS4yT2TfA0RPXeEbKTwTz1Dm7j-BUiRk_6CEEQznOCjOMaT2IxwBSPcQmztnj6N2Tjc4TqozDm5Oxwfb_Zrvx06vHuxoo1EuOe5AIBzcviV4tBgA2PyckutYG36KcCq4Ajt4uot_Wmtivo5rsEjPOAE9VmETUmfKgAqbFQcx_gcHKYsZbC_-2BWyZeADg'
    elif var == 'database_name':
        return 'movie_actor'
    elif var == 'database_path':
        return 'postgresql:///movie_actor'
    elif var == 'executive_producer':
        return 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkFEMVZrLU5pVkFvSmRvNmlOVnU1WCJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY29mZmVlLXByb2plY3QuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEwOTQyODg3MTQzMzk4NDkxMzU0IiwiYXVkIjoibW92aWVfcHJvamVjdCIsImlhdCI6MTU4ODk1Nzg0NSwiZXhwIjoxNTg5MDQ0MjQ1LCJhenAiOiJBSEZwdXM5cmthZHJwU2lXaXpLS3FCZWw2TE9maHJNOCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.bD-SVYJTFt5arl8lt7gBmSTOxmxlOHhHt-wIQjoxOLUB3KFv2IjBAUtOzXAWkNRJNipv0JG4No4PYYFB7GYYCV8myJP3t32zCEV3-GBTTgu_sG1eOSfrnCmfrrcxbK3SjbDiO7QfIZx3R48_iIiMXY1tJGKSie49saUefwrAsyBfinqSrtB9mpNzzZA9Blq_OM_nmnEY5BSvBYG-qOdMyfdFS7ZrOcVQlH3VQy3swicXpCZwsugMA_ghLdvZy4vuZQgWQF7swbp-HPRE8sGqJihJO0dHwqDpXO4B9nFT-M4BFLjH31ry_mkI9rUV-6qZVFb67JTbF6HhGFrNNaVsnA'
