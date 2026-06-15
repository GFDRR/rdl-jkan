---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: "Universidad de Cantabria, Instituto de Hidr\uCE58ulica Ambiental de la Universidad\
    \ de Cantabria 'IHCantabria'"
  url: www.ihcantabria.com
creator:
  affiliation: null
  email: null
  name: "Universidad de Cantabria, Instituto de Hidr\uCE58ulica Ambiental de la Universidad\
    \ de Cantabria 'IHCantabria'"
  url: www.ihcantabria.com
dataset_id: rdls_vln-coclico_cfhpallstats
description: 'This dataset combines local administrative units (LAUs) with NUTS2 and
  NUTS3 classifications and aggregates flood statistics for multiple scenarios. It
  includes high-defended, low-defended and unddefended flood scenarios with various
  return periods. The data is represented at the LAU level and includes connections
  to relevant NUTS and country boundaries, providing comprehensive flood exposure
  insights across Europe. [Source: This metadata record was automatically extracted
  from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: This dataset combines local administrative units (LAUs) with NUTS2
    and NUTS3 classifications and aggregates flood statistics for multiple scenarios.
    It includes high-defended, low-defended and unddefended flood scenarios with various
    return periods. The data is represented at the LAU level and includes connections
    to relevant NUTS and country boundaries, providing comprehensive flood exposure
    insights across Europe.
  sources:
  - id: source_1
    license: null
    name: "Universidad de Cantabria, Instituto de Hidr\uCE58ulica Ambiental de la\
      \ Universidad de Cantabria 'IHCantabria'"
    risk_data_type:
    - vulnerability
    type: dataset
    url: www.ihcantabria.com
    used_in: vulnerability
  - id: source_2
    license: null
    name: Eurostat
    risk_data_type:
    - vulnerability
    type: dataset
    url: https://ec.europa.eu/eurostat/web/nuts/local-administrative-units
    used_in: vulnerability
  - id: source_3
    license: null
    name: Deltares
    risk_data_type:
    - vulnerability
    type: dataset
    url: https://deltares.nl
    used_in: vulnerability
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: "Universidad de Cantabria, Instituto de Hidr\uCE58ulica Ambiental de la Universidad\
    \ de Cantabria 'IHCantabria'"
  url: www.ihcantabria.com
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: ref_citation
  name: None.
  url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/cfhp_all_stats/collection.json
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/cfhp_all_stats/collection.json
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
  title: 'STAC Collection: CoCliCo - Flood perspectives - statistics [cfhp_all_stats]'
- access_url: https://storage.googleapis.com/download/storage/v1/b/coclico-data-public/o/coclico%2Fassets%2Fthumbnails%2Fcfhp_all_stats.png?alt=media
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Flood perspectives - statistics
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
  description: CoCliCo - Flood perspectives - statistics (Snapshot of the collection's
    STAC items exported to GeoParquet format.)
  download_url: https://storage.googleapis.com/coclico-data-public/coclico/cfhp_all_stats/cfhp_all_stats.parquet
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
- vulnerability
schema: rdls-10
slug: rdls_vln-coclico_cfhpallstats
spatial:
  bbox:
  - -81.12146941539005
  - -29.12357316038395
  - 93.1752791130622
  - 37.855412297701754
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
title: CoCliCo - Flood perspectives - statistics
version: null
vulnerability: null
---
