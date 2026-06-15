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
dataset_id: rdls_exp-coclico_coastalgrid
description: "The Coastal Grid dataset provides a global tiling system for geospatial\
  \ analytics in coastal areas. It supports scalable data processing workflows by\
  \ offering structured grids at varying zoom levels (2, 3, 4, 5, 6, 7, 8, 9, 10)\
  \ and buffer sizes (500m, 1000m, 2000m, 5000m, 10000m, 15000m). Each tile contains\
  \ information on intersecting countries, continents, and Sentinel-2 MGRS tiles as\
  \ nested JSON lists. The dataset is particularly suited for applications requiring\
  \ global coastal coverage, such as satellite-based coastal monitoring, spatial analytics,\
  \ and large-scale data processing. Key Features: Global coverage of the coastal\
  \ zone, derived from OpenStreetMap's generalized coastline (2023-02). Precomputed\
  \ intersections with countries, continents, and MGRS tiles. Designed for use in\
  \ scalable geospatial workflows. This dataset is structured as a STAC collection,\
  \ with individual items for each zoom level and buffer size combination. Users can\
  \ filter items by the zoom and buffer_size fields in the STAC metadata. Please consider\
  \ the following citation when using this dataset: Floris Reinier Calkoen, Arjen\
  \ Pieter Luijendijk, Kilian Vos, Eti\xEBnne Kras, Fedor Baart, Enabling coastal\
  \ analytics at planetary scale, Environmental Modelling & Software, 2024, 106257,\
  \ ISSN 1364-8152, https://doi.org/10.1016/j.envsoft.2024.106257. [Source: This metadata\
  \ record was automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]"
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
  description: "The Coastal Grid dataset provides a global tiling system for geospatial\
    \ analytics in coastal areas. It supports scalable data processing workflows by\
    \ offering structured grids at varying zoom levels (2, 3, 4, 5, 6, 7, 8, 9, 10)\
    \ and buffer sizes (500m, 1000m, 2000m, 5000m, 10000m, 15000m). Each tile contains\
    \ information on intersecting countries, continents, and Sentinel-2 MGRS tiles\
    \ as nested JSON lists. The dataset is particularly suited for applications requiring\
    \ global coastal coverage, such as satellite-based coastal monitoring, spatial\
    \ analytics, and large-scale data processing. Key Features: Global coverage of\
    \ the coastal zone, derived from OpenStreetMap's generalized coastline (2023-02).\
    \ Precomputed intersections with countries, continents, and MGRS tiles. Designed\
    \ for use in scalable geospatial workflows. This dataset is structured as a STAC\
    \ collection, with individual items for each zoom level and buffer size combination.\
    \ Users can filter items by the zoom and buffer_size fields in the STAC metadata.\
    \ Please consider the following citation when using this dataset: Floris Reinier\
    \ Calkoen, Arjen Pieter Luijendijk, Kilian Vos, Eti\xEBnne Kras, Fedor Baart,\
    \ Enabling coastal analytics at planetary scale, Environmental Modelling & Software,\
    \ 2024, 106257, ISSN 1364-8152, https://doi.org/10.1016/j.envsoft.2024.106257."
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
loss:
  losses: []
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
  name: "Floris Reinier Calkoen, Arjen Pieter Luijendijk, Kilian Vos, Eti\xEBnne Kras,\
    \ Fedor Baart, Enabling coastal analytics at planetary scale, Environmental Modelling\
    \ & Software, 2024, 106257, ISSN 1364-8152, https://doi.org/10.1016/j.envsoft.2024.106257."
  url: https://doi.org/10.1016/j.envsoft.2024.106257
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/coastal-grid/collection.json
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
  title: 'STAC Collection: CoCliCo - Coastal Grid [coastal-grid]'
- access_url: https://coclico.blob.core.windows.net/assets/thumbnails/coastal-grid-thumbnail.jpeg
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Coastal Grid
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
  description: CoCliCo - Coastal Grid (Snapshot of the collection's STAC items exported
    to GeoParquet format.)
  download_url: https://coclico.blob.core.windows.net/items/coastal-grid.parquet
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
  description: CoCliCo - Coastal Grid (Web reference)
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
slug: rdls_exp-coclico_coastalgrid
spatial:
  bbox:
  - -180.0
  - -78.87279612057878
  - 180.0
  - 83.79921585603272
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
title: CoCliCo - Coastal Grid
version: null
vulnerability: null
---
