export interface Product {
  /** Unique ID of group of products. */
  slug: string;

  /** Title of a product. */
  title: string;

  /** Author of a product. */
  author: string;

  /** Url to cover image. */
  cover: string;

  /** Description of a product. */
  description: string;

  /** List of a product varieties. */
  products: ProductVariety[]
}

export enum ProductVarietyType {
  Digital = 'digital',
  Audio = 'audio',
  Printed = 'printed'
}

export interface ProductVariety {
  /** Unique product ID. */
  id: string;

  /** Type of a product variety. */
  type: ProductVarietyType;

  /** Price of a product */
  price: number;

  /** Name of variety */
  title: string;

  /** List of urls to download file */
  urls: UrlInfo[];

  series: string;
  year_published: number;
  publisher: string;
}

export interface UrlInfo {
  url: string;
  size: string;
  ext: string;
}

export const EmptyBook : Product = {
  slug: 'null', title: 'Empty book', author: 'No one', cover: '', description: '', products: []
}

export const EmptyProductVariety: ProductVariety = {
  id: '',
  price: -1,
  type: ProductVarietyType.Digital,
  title: '',
  urls: []
}
