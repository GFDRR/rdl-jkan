---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bejaia-et-tizi-ouzou-entre-le-11-et-le-
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bejaia-et-tizi-ouzou-entre-le-11-et-le-
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bejaia-et-tizi-ouzou-entre-le-11-et-le-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bejaia-et-tizi-ouzou-entre-le-11-et-le-
dataset_id: rdls_he-dza_unosat_densitedesfoyersdincendie_20210814
description: "UNOSAT code: FR20210811DZA Cette carte illustre la densit\xE9 des foyers\
  \ d'incendies d\xE9tect\xE9s \xE0 partir des donn\xE9es VIIRS acquise entre le 11\
  \ et le 13 ao\xFBt 2021. Les wilayas de Bejaia, Tizi Ouzou et Ain-Defla semblent\
  \ compter le plus grand nombre de foyers d'incendie avec respectivement 1,080; 573\
  \ et 190. En se basant sur les donn\xE9es d\xE9mographique Worldpop, environ 70,000\
  \ personnes dans la wilaya de Tizi Ouzou; 25,000 personnes dans la wilaya de Bejaia\
  \ et 13,000 personnes dans la wilaya de Skikda vivent \xE0 proximit\xE9 des foyers\
  \ d'incendie. Ceci est une analyse pr\xE9liminaire et n'as pas encore \xE9t\xE9\
  \ valid\xE9e sur le terrain. Ne pas h\xE9siter \xE0 envoyer vos commentaires au\
  \ Centre Satellitaire des Nations Unies (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bejaia-et-tizi-ouzou-entre-le-11-et-le-]"
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
    description: Population living in proximity to detected wildfire hotspots, derived
      from WorldPop demographic data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    wildfire:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: FWI:-
        process: wildfire
        trigger: null
        type: wildfire
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed VIIRS satellite imagery acquired between
    August 11-13, 2021 to detect and map active wildfire hotspots in three Algerian
    wilayas. Hotspot density was calculated by administrative boundary, and population
    exposure was estimated by intersecting hotspot locations with WorldPop gridded
    demographic data to quantify residents in proximity to fires.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bejaia-et-tizi-ouzou-entre-le-11-et-le-
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Algeria - Densit\xE9 des foyers d'incendies dans les wilayas de Bejaia\
    \ et Tizi Ouzou entre le 11 et le 13 ao\xFBt 2021 (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/DZ/FR20210811DZA/FR20210811DZA_gdb.zip
  format: Geodatabase
  id: resource_9a6c50d2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20210811DZA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Algeria - Densit\xE9 des foyers d'incendies dans les wilayas de Bejaia\
    \ et Tizi Ouzou entre le 11 et le 13 ao\xFBt 2021 (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/DZ/FR20210811DZA/FR20210811DZA_SHP.zip
  format: null
  id: resource_7bd86ae6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20210811DZA_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-dza_unosat_densitedesfoyersdincendie_20210814
spatial:
  bbox: null
  centroid: null
  countries:
  - DZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-08-14'
temporal_resolution: null
title: "Algeria - Densit\xE9 des foyers d'incendies dans les wilayas de Bejaia et\
  \ Tizi Ouzou entre le 11 et le 13 ao\xFBt 2021"
version: null
vulnerability: null
---
