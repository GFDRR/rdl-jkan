---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Deltares
  url: https://deltares.nl
creator:
  affiliation: null
  email: null
  name: Deltares
  url: https://deltares.nl
dataset_id: rdls_exp-coclico_coastalmask
description: 'Coastal mask that is derived from Copernicus elevation data combined
  with a maximum distanceto coastal water bodies. [Source: This metadata record was
  automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
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
license: ODbL-1.0
lineage:
  description: Coastal mask that is derived from Copernicus elevation data combined
    with a maximum distanceto coastal water bodies.
  sources:
  - id: source_1
    license: null
    name: Deltares
    risk_data_type:
    - exposure
    type: dataset
    url: https://deltares.nl
    used_in: exposure
  - id: source_2
    license: null
    name: Global Climate Forum
    risk_data_type:
    - exposure
    type: dataset
    url: https://globalclimateforum.org
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Deltares
  url: https://deltares.nl
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: ref_citation
  name: Lincke et al., 2023, in progress
  url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/coastal-mask/collection.json
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/coastal-mask/collection.json
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
  title: 'STAC Collection: CoCliCo - Coastal Mask [coastal-mask]'
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/assets/thumbnails/cm.png
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Coastal Mask
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
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-coclico_coastalmask
spatial:
  bbox:
  - -180.00041666666667
  - -60.000416666666666
  - 179.99958333333333
  - 84.99958333333333
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022'
  start: '2022'
temporal_resolution: null
title: CoCliCo - Coastal Mask
version: null
vulnerability: null
---
