---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/water-extents-in-maganja-da-costa-namacurra-nicoadala-districts-mozambique-as-of-17-march-
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extents-in-maganja-da-costa-namacurra-nicoadala-districts-mozambique-as-of-17-march-
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-maganja-da-costa-namacurra-nicoadala-districts-mozambique-as-of-17-march-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-maganja-da-costa-namacurra-nicoadala-districts-mozambique-as-of-17-march-
dataset_id: rdls_he-moz_unosat_detectedwaterextentsmagan_20220317
description: 'UNOSAT code: TC20220311MOZ This map illustrates satellite-detected surface
  waters in Maganja Da Costa, Namacurra & Nicoadala Districts, Zambezia Province,
  Mozambique as observed from a Sentinel-1 image acquired on 17 March 2022 at 05:00
  local time. Within the analyzed area of about 6,970 km2, about 442 km2 of lands
  appear to be flooded. Based on Worldpop population data and the detected surface
  waters, about 36,500 people are potentially exposed or living close to flooded areas.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to United Nations Satellite Centre (UNOSAT). Important note:
  Flood analysis from radar images may underestimate the presence of standing waters
  in built-up areas and densely vegetated areas due to backscattering properties of
  the radar signal.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-maganja-da-costa-namacurra-nicoadala-districts-mozambique-as-of-17-march-]'
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
    description: Population potentially exposed or living close to detected flooded
      areas, estimated at 36,500 people using WorldPop data
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-1 SAR imagery acquired on 17 March 2022 was analyzed by UNOSAT\
    \ analysts using change detection methods to identify surface water extents across\
    \ 6,970 km\xB2 in Zambezia Province. Detected water areas (442 km\xB2) were intersected\
    \ with WorldPop population data to estimate exposure. This is a preliminary post-event\
    \ assessment not yet validated in the field."
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
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-in-maganja-da-costa-namacurra-nicoadala-districts-mozambique-as-of-17-march-
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
  description: Satellite detected water extents in Maganja Da Costa, Namacurra & Nicoadala
    Districts, Mozambique as of 17 March 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/MZ/TC20220311MOZ/TC20220311MOZ_gdb.zip
  format: Geodatabase
  id: resource_bc87d114
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220311MOZ_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Maganja Da Costa, Namacurra & Nicoadala
    Districts, Mozambique as of 17 March 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/MZ/TC20220311MOZ/TC20220311MOZ_SHP.zip
  format: null
  id: resource_42359599
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220311MOZ_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-moz_unosat_detectedwaterextentsmagan_20220317
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-03-17'
temporal_resolution: null
title: Satellite detected water extents in Maganja Da Costa, Namacurra & Nicoadala
  Districts, Mozambique as of 17 March 2022
version: null
vulnerability: null
---
