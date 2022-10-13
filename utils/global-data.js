export const getGlobalData = () => {
  const name = process.env.BLOG_NAME
    ? decodeURI(process.env.BLOG_NAME)
    : 'Air and Steel';
  const blogTitle = process.env.BLOG_TITLE
    ? decodeURI(process.env.BLOG_TITLE)
    : 'Aaron Steel\'s Resources, Playbooks, and Documentation in the Fight for the Future.';
  const footerText = process.env.BLOG_FOOTER_TEXT
    ? decodeURI(process.env.BLOG_FOOTER_TEXT)
    : 'Hi! Aaron, nice to meet ya. This site is where I\'m documenting as I go, in order to keep my learnings and thoughts in an easily accessible digital notebook. My purpose in life is organizing (engineering, if you will) and building the change I want to see in the world; to help as much as possible, while I\'ve got the chance to do it.';

  return {
    name,
    blogTitle,
    footerText,
  };
};
