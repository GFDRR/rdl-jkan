---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Eurostat
  url: https://ec.europa.eu/eurostat/web/gisco/geodata/statistical-units/territorial-units-statistics
creator:
  affiliation: null
  email: null
  name: Eurostat
  url: https://ec.europa.eu/eurostat/web/gisco/geodata/statistical-units/territorial-units-statistics
dataset_id: rdls_exp-coclico_nuts
description: 'The GISCO statistical unit dataset represents the NUTS (nomenclature
  of territorial units for statistics) and statistical regions by means of multipart
  polygon, polyline and point topology. The NUTS geographical information is completed
  by attribute tables and a set of cartographic help lines to better visualise multipart
  polygonal regions. [Source: This metadata record was automatically extracted from
  the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure:
- asset_type:
    description: land use/land cover footprints
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: square_metre
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: The GISCO statistical unit dataset represents the NUTS (nomenclature
    of territorial units for statistics) and statistical regions by means of multipart
    polygon, polyline and point topology. The NUTS geographical information is completed
    by attribute tables and a set of cartographic help lines to better visualise multipart
    polygonal regions.
  sources:
  - id: source_1
    license: null
    name: Eurostat
    risk_data_type:
    - exposure
    type: dataset
    url: https://ec.europa.eu/eurostat/web/gisco/geodata/statistical-units/territorial-units-statistics
    used_in: exposure
  - id: source_2
    license: null
    name: Deltares
    risk_data_type:
    - exposure
    type: dataset
    url: https://deltares.nl
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Eurostat
  url: https://ec.europa.eu/eurostat/web/gisco/geodata/statistical-units/territorial-units-statistics
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: ref_citation
  name: None.
  url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/NUTS/collection.json
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/NUTS/collection.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Collection metadata for this dataset, hosted as part of
    the CoCliCo catalog. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_collection
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Collection: CoCliCo - Nomenclature of territorial units for statistics
    [NUTS]'
- access_url: https://storage.googleapis.com/download/storage/v1/b/coclico-data-public/o/coclico%2Fassets%2Fthumbnails%2FNUTS.png?alt=media
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Nomenclature of territorial units for statistics
  download_url: null
  format: null
  id: resource_thumbnail
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Thumbnail
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Nomenclature of territorial units for statistics (Snapshot
    of the collection's STAC items exported to GeoParquet format.)
  download_url: gs://coclico-data-public/coclico/NUTS/NUTS_RG_01M_2021_3035.parquet
  format: null
  id: resource_geoparquetstacitems
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoParquet STAC items
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-coclico_nuts
spatial:
  bbox:
  - -90.23528381409483
  - -29.857082115784582
  - 103.456913582018
  - 39.79889221318682
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024'
  start: '2024'
temporal_resolution: null
title: CoCliCo - Nomenclature of territorial units for statistics
version: null
vulnerability: null
---
