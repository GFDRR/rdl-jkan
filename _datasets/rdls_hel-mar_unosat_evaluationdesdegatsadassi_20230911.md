---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/evaluation-des-degats-a-adassil-region-de-chichaoua-province-de-marrakech-safi-maroc-au-10
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/evaluation-des-degats-a-adassil-region-de-chichaoua-province-de-marrakech-safi-maroc-au-10
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/evaluation-des-degats-a-adassil-region-de-chichaoua-province-de-marrakech-safi-maroc-au-10
dataset_id: rdls_hel-mar_unosat_evaluationdesdegatsadassi_20230911
description: "UNOSAT code EQ20230909MAR, GDACS Id: 1390643 Cette carte illustre les\
  \ structures/b\xE2timents potentiellement endommag\xE9s par le s\xE9isme de magnitude\
  \ 6,8 d' Adassil/Mjdid du 8 Septembre 2023 \xE0 22h11 UTC (\xE0 75 km au SO de Marrakech)\
  \ tel qu'observ\xE9 \xE0 partir d'une image satellite Pl\xE9iades acquise le 10\
  \ Septembre 2023. Dans ce secteur d'analyse, UNOSAT a identifi\xE9 216 b\xE2timents\
  \ endommag\xE9s et/ou potentiellement endommag\xE9s. Ceci est une analyse pr\xE9\
  liminaire et n'a pas encore \xE9t\xE9 valid\xE9e sur le terrain. Ne pas h\xE9siter\
  \ \xE0 envoyer vos commentaires au Centre Satellitaire des Nations Unies (UNOSAT).\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/evaluation-des-degats-a-adassil-region-de-chichaoua-province-de-marrakech-safi-maroc-au-10]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Building stock in Adassil region, Chichaoua province, classified
      by damage status
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
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts compared pre- and post-event Pl\xE9iades satellite\
    \ imagery acquired on 10 September 2023 to identify structural damage from the\
    \ 8 September 2023 magnitude 6.8 earthquake near Marrakech. Building footprints\
    \ were manually delineated and classified by damage status to produce a preliminary\
    \ damage assessment map."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/evaluation-des-degats-a-adassil-region-de-chichaoua-province-de-marrakech-safi-maroc-au-10
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from the 8 September 2023 Adassil earthquake
      assessed via satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
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
  description: "Morocco - \xC9valuation des d\xE9gats \xE0 Adassil, r\xE9gion de Chichaoua,\
    \ province de Marrakech-Safi, Maroc, au 10 Septembre 2023 (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/3666/EQ20230909MAR_gdb.zip
  format: Geodatabase
  id: resource_43cac4b3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230909MAR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Morocco - \xC9valuation des d\xE9gats \xE0 Adassil, r\xE9gion de Chichaoua,\
    \ province de Marrakech-Safi, Maroc, au 10 Septembre 2023 (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/3666/EQ20230909MAR_SHP.zip
  format: null
  id: resource_631eef2f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230909MAR_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mar_unosat_evaluationdesdegatsadassi_20230911
spatial:
  bbox: null
  centroid: null
  countries:
  - MAR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-09-11'
temporal_resolution: null
title: "Morocco - \xC9valuation des d\xE9gats \xE0 Adassil, r\xE9gion de Chichaoua,\
  \ province de Marrakech-Safi, Maroc, au 10 Septembre 2023"
version: null
vulnerability: null
---
