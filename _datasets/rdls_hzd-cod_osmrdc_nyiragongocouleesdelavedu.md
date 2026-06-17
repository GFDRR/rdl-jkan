---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 (ESA Copernicus)
    url: https://data.humdata.org/dataset/nyiragongo-coulees-de-lave-du-22-mai-2021
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Maxar high-resolution imagery
    url: https://data.humdata.org/dataset/nyiragongo-coulees-de-lave-du-22-mai-2021
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OpenStreetMap RDC
  url: https://data.humdata.org/dataset/nyiragongo-coulees-de-lave-du-22-mai-2021
creator:
  affiliation: null
  email: null
  name: OpenStreetMap RDC
  url: https://data.humdata.org/dataset/nyiragongo-coulees-de-lave-du-22-mai-2021
dataset_id: rdls_hzd-cod_osmrdc_nyiragongocouleesdelavedu
description: "Cette premi\xE8re version des coul\xE9es de lave r\xE9sultant de l'\xE9\
  ruption du volcan Nyiragongo du 22 mai 2021 sont des donn\xE9es approximatives.\
  \ Elles ont \xE9t\xE9 num\xE9ris\xE9es sur base des donn\xE9es Sentinel-1 du 25\
  \ mai 2021. [UPDATE 27/05/2021] Une version l\xE9g\xE8rement adapt\xE9e au niveau\
  \ de l'extr\xE9mit\xE9 Sud de la coul\xE9e ayant atteint Buhene est d\xE9sormais\
  \ disponible. La mise \xE0 jour \xE0 \xE9t\xE9 effectu\xE9e sur base d'une image\
  \ Maxar haute-r\xE9solution du 25 mai 2021.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/nyiragongo-coulees-de-lave-du-22-mai-2021]"
details: "Ces donn\xE9es sont approximatives, la pr\xE9cision devrait s'am\xE9liorer\
  \ au fur et \xE0 mesure des mises \xE0 jour."
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: lava
      trigger: null
      type: volcanic
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: volcanic
license: ODbL-1.0/
lineage:
  description: Lava flow polygons were manually digitized by OpenStreetMap RDC from
    Sentinel-1 SAR data acquired on 25 May 2021, three days after the Nyiragongo eruption
    of 22 May 2021. A subsequent update refined the southern boundary of the flow
    near Buhene using a Maxar high-resolution optical image from the same date. The
    resulting vector dataset represents the approximate spatial extent of lava flows
    for emergency mapping and disaster response purposes.
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 (ESA Copernicus)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Maxar high-resolution imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/nyiragongo-coulees-de-lave-du-22-mai-2021
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "DR Congo - Nyiragongo Coul\xE9es de lave du 22 mai 2021 (Shapefile\
    \ zipp\xE9, mise \xE0 jour du 27 mai)"
  download_url: https://data.humdata.org/dataset/035b0a01-3295-4223-a67e-f6b35751defa/resource/4c725307-f3e0-4d32-a19e-4555d7ad2dd5/download/nyiragongo_lave_sentinel-maxar_210525.zip
  format: null
  id: resource_4c725307
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nyiragongo_Lave_Sentinel-Maxar_210525.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "DR Congo - Nyiragongo Coul\xE9es de lave du 22 mai 2021 (Donn\xE9\
    es au format .osm)"
  download_url: https://data.humdata.org/dataset/035b0a01-3295-4223-a67e-f6b35751defa/resource/447405bd-ac74-4e5a-98f8-4fa64b763b4e/download/lave_sentinel-maxar_210525.osm
  format: OSMand OBF
  id: resource_447405bd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Lave_Sentinel-Maxar_210525.osm
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-cod_osmrdc_nyiragongocouleesdelavedu
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: "DR Congo - Nyiragongo Coul\xE9es de lave du 22 mai 2021"
version: null
vulnerability: null
---
