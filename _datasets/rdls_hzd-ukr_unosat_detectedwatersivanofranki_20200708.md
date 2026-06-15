---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/waters-in-ivano-frankivska-and-ternopilska-oblast-of-ukraine-as-of-24-june-2020
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-in-ivano-frankivska-and-ternopilska-oblast-of-ukraine-as-of-24-june-2020
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/waters-in-ivano-frankivska-and-ternopilska-oblast-of-ukraine-as-of-24-june-2020
dataset_id: rdls_hzd-ukr_unosat_detectedwatersivanofranki_20200708
description: 'UNOSAT code: FL20200626UKR This map illustrates satellite-detected surface
  waters in Ivano-Frankivska and Ternopilska Oblastof Ukraine as observed from a Sentinel-1
  image acquired on 24 June 2020. Within the ana lyzed area of about 642 km2, a total
  of a bout 35 km2 of lands appear to be flooded. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT
  .. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/waters-in-ivano-frankivska-and-ternopilska-oblast-of-ukraine-as-of-24-june-2020]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
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
  description: "UNOSAT analysts processed Sentinel-1 SAR imagery acquired on 24 June\
    \ 2020 over Ivano-Frankivska and Ternopilska Oblasts, comparing satellite images\
    \ to detect notable changes in surface water extent. The analysis identified flooded\
    \ areas within a 642 km\xB2 study region and quantified inundation extent as approximately\
    \ 35 km\xB2, delivered as vector geodatabase and shapefile formats with area measurements."
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
- href: https://data.humdata.org/dataset/waters-in-ivano-frankivska-and-ternopilska-oblast-of-ukraine-as-of-24-june-2020
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
  description: Satellite detected waters in Ivano-Frankivska and Ternopilska Oblast
    of Ukraine as of 24 June 2020 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/UA/FL20200626UKR/FL20200626UKR_gdb.zip
  format: Geodatabase
  id: resource_5a8ba619
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200626UKR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters in Ivano-Frankivska and Ternopilska Oblast
    of Ukraine as of 24 June 2020 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/UA/FL20200626UKR/FL20200626UKR_SHP.zip
  format: null
  id: resource_29aeccd2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200626UKR_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ukr_unosat_detectedwatersivanofranki_20200708
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-07-08'
temporal_resolution: null
title: Satellite detected waters in Ivano-Frankivska and Ternopilska Oblast of Ukraine
  as of 24 June 2020
version: null
vulnerability: null
---
