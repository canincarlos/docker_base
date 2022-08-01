import { api } from '../config'
import ArticleList from '../components/ArticleList'

export default function Home({ articles }) {
  return (
    <div>
      <ArticleList articles={articles} />
    </div>
  )
}

export const getStaticProps = async () => {
  const res = await fetch(`${api}/gettweets`)
  const articles_set = await res.json()
  const articles = articles_set.results
  // console.log("hello: ", articles)

  return {
    props: {
      articles,
    },
  }
}