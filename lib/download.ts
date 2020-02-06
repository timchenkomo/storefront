import { Group, Product } from '@/lib/book.ts'

// Sample : /sample/{product_slug}.{ext} : {product_slug}/sample.{ext}
// Product: /{product_slug}.{ext}        : {product_slug}/{product_slug}.{ext}
// Reader : /{product_slug}.epub         : {product_slug}/{product_slug}.epub

export function getSampleUrl(product: Product, ext: string) {
  return '/api/download/' + product.slug + '/sample.' + ext
}

export function getProductUrl(product: Product, ext: string) {
  return '/api/download/' + product.slug + '.' + ext
}

export function getReaderUrl(product: Product) {
  // reader supports epub format only
  return getSampleUrl(product, 'epub')
}
