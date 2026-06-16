---
attributions:
- entity:
    affiliation: null
    email: null
    name: VIIRS (Visible Infrared Imaging Radiometer Suite)
    url: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bouira-tizi-ouzou-et-bejaia-le-24-juill
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bouira-tizi-ouzou-et-bejaia-le-24-juill
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bouira-tizi-ouzou-et-bejaia-le-24-juill
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bouira-tizi-ouzou-et-bejaia-le-24-juill
dataset_id: rdls_hel-dza_unosat_densitedesfoyersdincendie_20230725
description: "UNOSAT code FR20230724DZA, GDACS Id: 1015944 Cette carte illustre la\
  \ densit\xE9 des foyers d'incendies d\xE9tect\xE9s \xE0 partir des donn\xE9es VIIRS\
  \ acquises le 24 juillet 2023. Les wilayas de Bouira, Bejaia et Skikda semblent\
  \ compter le plus grand nombre de foyers d'incendie avec respectivement 398; 320\
  \ et 108. En se basant sur les donn\xE9es d\xE9mographiques Worldpop, environ 44,000\
  \ personnes dans la wilaya de Skikda; 20,000 personnes dans la wilaya de Bejaia\
  \ et 14,000 personnes dans la wilaya de Bouira vivent \xE0 proximit\xE9 des foyers\
  \ d'incendie. Ceci est une analyse pr\xE9liminaire et n'a pas encore \xE9t\xE9 valid\xE9\
  e sur le terrain. Ne pas h\xE9siter \xE0 envoyer vos commentaires au Centre Satellitaire\
  \ des Nations Unies (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bouira-tizi-ouzou-et-bejaia-le-24-juill]"
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
    description: Residential population living in proximity to detected wildfire hotspots
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
  event_sets:
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts detected active wildfire hotspots from VIIRS thermal
    satellite imagery acquired on 24 July 2023. Hotspot locations were spatially intersected
    with WorldPop gridded population data to estimate the number of residents living
    in proximity to detected fires across three Algerian wilayas (Bouira, Bejaia,
    Skikda).
  sources:
  - id: source_1
    license: null
    name: VIIRS (Visible Infrared Imaging Radiometer Suite)
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
- href: https://data.humdata.org/dataset/densite-des-foyers-d-incendies-dans-les-wilayas-de-bouira-tizi-ouzou-et-bejaia-le-24-juill
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to wildfire hotspots in Bouira, Bejaia, and Skikda
      wilayas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
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
  description: "Algeria - Densit\xE9 des foyers d'incendies dans les wilayas de Bouira,\
    \ Tizi Ouzou et Bejaia le 24 juillet 2023 (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/3641/FR20230724DZA_gdb.zip
  format: Geodatabase
  id: resource_7b3340de
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20230724DZA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Algeria - Densit\xE9 des foyers d'incendies dans les wilayas de Bouira,\
    \ Tizi Ouzou et Bejaia le 24 juillet 2023 (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/3641/FR20230724DZA_SHP.zip
  format: null
  id: resource_b46797ab
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20230724DZA_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Algeria - Densit\xE9 des foyers d'incendies dans les wilayas de Bouira,\
    \ Tizi Ouzou et Bejaia le 24 juillet 2023 (Excel file)"
  download_url: https://unosat.org/static/unosat_filesystem/3641/UNOSAT_PopulationExposed_Hotspots_FR20230724DZA_25072023.xlsx
  format: null
  id: resource_10d4f8b8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposed_Hotspots_FR20230724DZA_25072023.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-dza_unosat_densitedesfoyersdincendie_20230725
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
  start: '2023-07-25'
temporal_resolution: null
title: "Algeria - Densit\xE9 des foyers d'incendies dans les wilayas de Bouira, Tizi\
  \ Ouzou et Bejaia le 24 juillet 2023"
version: null
vulnerability: null
---
