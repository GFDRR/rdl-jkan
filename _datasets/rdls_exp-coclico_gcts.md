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
dataset_id: rdls_exp-coclico_gcts
description: 'Cross-shore coastal transects are essential to coastal monitoring, offering
  a consistent reference line to measure coastal change, while providing a robust
  foundation to map coastal characteristics and derive coastal statistics thereof.
  The Global Coastal Transect System consists of more than 11 million cross-shore
  coastal transects uniformly spaced at 100-m intervals alongshore, for all OpenStreetMap
  coastlines that are longer than 5 kilometers. The dataset is more extensively described
  Calkoen et al., 2024. ''Enabling Coastal Analytics at Planetary Scale'' available
  here (https://doi.org/10.1016/j.envsoft.2024.106257). [Source: This metadata record
  was automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure:
- asset_type:
    description: infrastructure footprints
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: Cross-shore coastal transects are essential to coastal monitoring,
    offering a consistent reference line to measure coastal change, while providing
    a robust foundation to map coastal characteristics and derive coastal statistics
    thereof. The Global Coastal Transect System consists of more than 11 million cross-shore
    coastal transects uniformly spaced at 100-m intervals alongshore, for all OpenStreetMap
    coastlines that are longer than 5 kilometers. The dataset is more extensively
    described Calkoen et al., 2024. 'Enabling Coastal Analytics at Planetary Scale'
    available here (https://doi.org/10.1016/j.envsoft.2024.106257).
  sources:
  - id: source_1
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
  doi: 10.1016/j.envsoft.2024.106257
  id: ref_pub_1
  name: "Floris Reinier Calkoen, Arjen Pieter Luijendijk, Kilian Vos, Eti\xC3\xAB\
    nne Kras, Fedor Baart, Enabling coastal analytics at planetary scale, Environmental\
    \ Modelling & Software, 2024, 106257, ISSN 1364-8152, https://doi.org/10.1016/j.envsoft.2024.106257."
  url: https://doi.org/10.1016/j.envsoft.2024.106257
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/gcts/collection.json
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
  title: 'STAC Collection: CoCliCo - Global Coastal Transect System (GCTS) [gcts]'
- access_url: https://coclico.blob.core.windows.net/assets/thumbnails/gcts-thumbnail.jpeg
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Global Coastal Transect System (GCTS)
  download_url: null
  format: null
  id: resource_thumbnail
  media_type: image/jpeg
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
  description: CoCliCo - Global Coastal Transect System (GCTS) (Snapshot of the collection's
    STAC items exported to GeoParquet format.)
  download_url: az://items/gcts.parquet
  format: null
  id: resource_geoparquetstacitems
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoParquet STAC items
- access_url: https://doi.org/10.1016/j.envsoft.2024.106257
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Global Coastal Transect System (GCTS) (Web reference)
  download_url: null
  format: Web reference
  id: resource_link_reference
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Reference
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-coclico_gcts
spatial:
  bbox:
  - -179.99979945991507
  - -78.74747176732404
  - 179.9998718338963
  - 83.66967471602302
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023'
  start: '2023'
temporal_resolution: null
title: CoCliCo - Global Coastal Transect System (GCTS)
version: null
vulnerability: null
---
