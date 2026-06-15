---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian OpenStreetMap Team (HOTOSM) Asia Pacific
    url: https://data.humdata.org/dataset/tm-open-buildings-philippines
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Thinking Machines Data Science
  url: https://data.humdata.org/dataset/tm-open-buildings-philippines
creator:
  affiliation: null
  email: null
  name: Thinking Machines Data Science
  url: https://data.humdata.org/dataset/tm-open-buildings-philippines
dataset_id: rdls_exp-phl_tmds_tmopenbuildings_2023
description: 'Thinking Machines Data Science is releasing TM Open Buildings, a dataset
  of manually-drawn building outlines covering 12 Philippine cities with detailed
  annotations on building and roof attributes as seen over satellite imagery. We contribute
  the buildings in OpenStreetMap and also made available for download in Kaggle. This
  is made possible with the support from the Lacuna Fund .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/tm-open-buildings-philippines]'
details: You may view more details of our process in our [wiki page](https://wiki.openstreetmap.org/wiki/TM_Open_Buildings).
  Kindly use our Github [Issues tab](https://github.com/thinkingmachines/ph-open-buildings/issues)
  to file any specific concerns about the dataset.
exposure:
- asset_type:
    description: Manually-drawn building footprints with structural attributes including
      height, roof material, roof layout, and settlement type across 12 Philippine
      cities
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Building footprints were manually digitized from satellite imagery
    by Thinking Machines Data Science for 12 Philippine cities. Structural attributes
    (height, roof material, roof layout, roof area, settlement type, gating status)
    were annotated during digitization. The dataset was validated in consultation
    with HOTOSM Asia Pacific and Philippine Action for Community-led Shelter Initiatives
    (PACSII) to ensure attribute accuracy and consistency with OpenStreetMap standards.
  sources:
  - id: source_1
    license: null
    name: Thinking Machines Data Science
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Humanitarian OpenStreetMap Team (HOTOSM) Asia Pacific
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tm-open-buildings-philippines
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://www.hotosm.org/where-we-work/philippines/
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://wiki.openstreetmap.org/wiki/TM_Open_Buildings
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: https://docs.google.com/spreadsheets/d/1jLoGUtnd1qyvqN43uQEtCo0C4x2QR3DkSKolH2ep_uU/
- author_names: null
  date_published: null
  doi: null
  id: reference_4
  name: Methodology documentation
  url: https://www.mapbox.com/maps/satellite
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Philippines - TM Open Buildings (A dataset of manually-drawn building
    outlines covering 12 Philippine cities)
  download_url: https://data.humdata.org/dataset/372bacbb-ab2c-464a-ad38-bd2034393bec/resource/5baa6bbb-8972-46c9-89c3-1ec114864d5e/download/tm_open_bldgs_2023.geojson
  format: null
  id: resource_5baa6bbb
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tm_open_bldgs_2023.geojson
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-phl_tmds_tmopenbuildings_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-09-30'
  start: '2023-08-01'
temporal_resolution: null
title: Philippines - TM Open Buildings
version: null
vulnerability: null
---
