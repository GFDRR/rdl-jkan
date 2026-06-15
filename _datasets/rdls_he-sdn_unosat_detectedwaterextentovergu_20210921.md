---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-over-guli-district-white-nile-state-of-sudan-as-of-19-september-2021
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-guli-district-white-nile-state-of-sudan-as-of-19-september-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-guli-district-white-nile-state-of-sudan-as-of-19-september-2021
dataset_id: rdls_he-sdn_unosat_detectedwaterextentovergu_20210921
description: 'UNOSAT code: FL20210907SDN This map illustrates satellite detected waters
  and the related potentially affected croplands as deduced using a Sentinel-2 satellite
  image acquired on 19 September 2021 over the Guli District, White Nile State of
  Sudan. The water extent appears to have decreased of about 70 km2 since 14 September
  2021. In this area, about 36 km2 of croplands appear to be likely affected by the
  flood waters. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to United Nations Satellite Centre (UNOSAT).
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-guli-district-white-nile-state-of-sudan-as-of-19-september-2021]'
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
    description: Croplands potentially affected by flood waters in the study area
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-2 satellite imagery acquired on 19 September 2021 was analyzed
    by UNOSAT to detect water extent through multi-temporal comparison with imagery
    from 14 September 2021. Analysts identified flooded areas and overlaid cropland
    layers to estimate affected agricultural land (36 km2), with water extent showing
    a 70 km2 decrease over the 5-day period.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-over-guli-district-white-nile-state-of-sudan-as-of-19-september-2021
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
  description: Satellite detected water extent over Guli District, White Nile State
    of Sudan as of 19 September 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/SD/FL20210907SDN/FL20210907SDN_gdb.zip
  format: Geodatabase
  id: resource_edcfdb60
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210907SDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Guli District, White Nile State
    of Sudan as of 19 September 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/SD/FL20210907SDN/FL20210907SDN_SHP.zip
  format: null
  id: resource_884d007e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210907SDN_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-sdn_unosat_detectedwaterextentovergu_20210921
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-09-21'
temporal_resolution: null
title: Satellite detected water extent over Guli District, White Nile State of Sudan
  as of 19 September 2021
version: null
vulnerability: null
---
