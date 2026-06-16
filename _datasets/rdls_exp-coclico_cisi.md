---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Deltares
  url: https://www.deltares.nl
creator:
  affiliation: null
  email: null
  name: Deltares
  url: https://www.deltares.nl
dataset_id: rdls_exp-coclico_cisi
description: "Critical infrastructure (CI) is fundamental for the functioning of a\
  \ society and forms the backbone for socio-economic development. Natural and human-made\
  \ threats, however, pose a major risk to CI. Therefore, geospatial data on the location\
  \ of CI are fundamental for in-depth risk analyses, which are required to inform\
  \ policy decisions aiming to reduce risk. We present a first-of-its-kind globally\
  \ harmonized spatial dataset for the representation of CI. In this study, we: (1)\
  \ collect and harmonize detailed geospatial data of the world's main CI systems\
  \ into a single geospatial database; and (2) develop the Critical Infrastructure\
  \ Spatial Index (CISI) to express the global spatial intensity of CI. The CISI aggregates\
  \ high-resolution geospatial OpenStreetMap (OSM) data of 39 CI types that are categorized\
  \ under seven overarching CI systems. The detailed geospatial data are rasterized\
  \ into a harmonized and consistent dataset with a resolution of 0.10 \xD7 0.10.\
  \ Variants in the source dataset - x: -179.94999999999996, 179.95000000000007; y:\
  \ 32.608332820000165, 80.70833282000017. [Source: This metadata record was automatically\
  \ extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]"
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
license: https://example.org/license/unknown
lineage:
  description: "Critical infrastructure (CI) is fundamental for the functioning of\
    \ a society and forms the backbone for socio-economic development. Natural and\
    \ human-made threats, however, pose a major risk to CI. Therefore, geospatial\
    \ data on the location of CI are fundamental for in-depth risk analyses, which\
    \ are required to inform policy decisions aiming to reduce risk. We present a\
    \ first-of-its-kind globally harmonized spatial dataset for the representation\
    \ of CI. In this study, we: (1) collect and harmonize detailed geospatial data\
    \ of the world's main CI systems into a single geospatial database; and (2) develop\
    \ the Critical Infrastructure Spatial Index (CISI) to express the global spatial\
    \ intensity of CI. The CISI aggregates high-resolution geospatial OpenStreetMap\
    \ (OSM) data of 39 CI types that are categorized under seven overarching CI systems.\
    \ The detailed geospatial data are rasterized into a harmonized and consistent\
    \ dataset with a resolution of 0.10 \xD7 0.10."
  sources:
  - id: source_1
    license: null
    name: Deltares
    risk_data_type:
    - exposure
    type: dataset
    url: https://www.deltares.nl
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
  url: https://www.deltares.nl
purpose: null
referenced_by: []
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/cisi/collection.json
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
  title: 'STAC Collection: CoCliCo - Critical Infrastructure Spatial Index [cisi]'
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/assets/thumbnails/cisi.png
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Critical Infrastructure Spatial Index
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
slug: rdls_exp-coclico_cisi
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: CoCliCo - Critical Infrastructure Spatial Index
version: null
vulnerability: null
---
