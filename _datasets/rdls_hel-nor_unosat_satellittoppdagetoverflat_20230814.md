---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/satellittoppdaget-overflatevann-langs-med-gudbrandsdalslagen-ringebu-sor-fron-og-nord-fron
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellittoppdaget-overflatevann-langs-med-gudbrandsdalslagen-ringebu-sor-fron-og-nord-fron
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellittoppdaget-overflatevann-langs-med-gudbrandsdalslagen-ringebu-sor-fron-og-nord-fron
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellittoppdaget-overflatevann-langs-med-gudbrandsdalslagen-ringebu-sor-fron-og-nord-fron
dataset_id: rdls_hel-nor_unosat_satellittoppdagetoverflat_20230814
description: "UNOSAT code FL20230811NOR ette kartet viser kumulativt satellittoppdaget\
  \ overflatevann langs med Gudbrandsdalsl\xE5gen i Ringebu, S\xF8r-Fron og Nord-Fron\
  \ kommune, Innlandet fylke, Norge, observert fra et Sentinel-1 bilde tatt den 10.\
  \ august 2023 kl. 17:03 UTC. Innenfor det analyserte omr\xE5det p\xE5 omtrent 500\
  \ km\xB2, er omtrent 15 km\xB2 med land observert som oversv\xF8mt. Basert p\xE5\
  \ befolkningsdata fra Worldpop og det kartlagte overflatevannet er omtrent 800 personer\
  \ potensielt eksponert eller bor i n\xE6rheten av det oversv\xF8mte omr\xE5der.\
  \ Dette er en forel\xF8pig analyse og er enn\xE5 ikke validert p\xE5 feltet. Vennligst\
  \ send tilbakemelding fra bakken til FNs satellittsenter (UNOSAT).. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/satellittoppdaget-overflatevann-langs-med-gudbrandsdalslagen-ringebu-sor-fron-og-nord-fron]"
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
    description: Residential population potentially exposed to or residing near inundated
      areas, derived from WorldPop data
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
    flood:
    - analysis_type: probabilistic
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts processed Sentinel-1 SAR imagery from 10 August 2023\
    \ to detect surface water extent along Gudbrandsdalsl\xE5gen river through change\
    \ detection analysis. Inundated areas (approximately 15 km\xB2) were mapped within\
    \ the study region. Population exposure was estimated by overlaying the mapped\
    \ water extent with WorldPop gridded population data, yielding approximately 800\
    \ potentially affected persons."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 satellite imagery
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
- href: https://data.humdata.org/dataset/satellittoppdaget-overflatevann-langs-med-gudbrandsdalslagen-ringebu-sor-fron-og-nord-fron
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Approximately 800 persons potentially exposed or residing near fluvial
      flood-inundated areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
  description: "Norway - Satellittoppdaget overflatevann langs med Gudbrandsdalsl\xE5\
    gen, Ringebu, S\xF8r-Fron og Nord-Fron Kommune, Innlandet Fylke, Norge (Zipped\
    \ geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/3656/FL20230811NOR_gdb.zip
  format: Geodatabase
  id: resource_ae70888a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230811NOR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Norway - Satellittoppdaget overflatevann langs med Gudbrandsdalsl\xE5\
    gen, Ringebu, S\xF8r-Fron og Nord-Fron Kommune, Innlandet Fylke, Norge (Zipped\
    \ shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/3656/FL20230811NOR_SHP.zip
  format: null
  id: resource_c9a2b2cc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230811NOR_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-nor_unosat_satellittoppdagetoverflat_20230814
spatial:
  bbox: null
  centroid: null
  countries:
  - NOR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-08-14'
temporal_resolution: null
title: "Norway - Satellittoppdaget overflatevann langs med Gudbrandsdalsl\xE5gen,\
  \ Ringebu, S\xF8r-Fron og Nord-Fron Kommune, Innlandet Fylke, Norge"
version: null
vulnerability: null
---
