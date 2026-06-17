---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2
    url: https://data.humdata.org/dataset/water-extents-in-midongy-atsimo-district-atsimo-atsinanana-region-madagascar-as-of-24-febr
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extents-in-midongy-atsimo-district-atsimo-atsinanana-region-madagascar-as-of-24-febr
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-midongy-atsimo-district-atsimo-atsinanana-region-madagascar-as-of-24-febr
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-midongy-atsimo-district-atsimo-atsinanana-region-madagascar-as-of-24-febr
dataset_id: rdls_he-mdg_unosat_detectedwaterextentsmidon_20220304
description: 'UNOSAT code: TC20220221MDG This map illustrates satellite-detected surface
  waters in Midongy-Atsimo District, Atsimo Atsinanana Region, Madagascar as observed
  from a Sentinel-2 image acquired on 24 February 2022 at 10:00 local time. Within
  the analyzed area about 1,200 km2, a total of about 90 km2 of lands appear to be
  flooded. Based on Worldpop population data and the detected surface waters, about
  5,000 people are potentially exposed or living close to flooded areas. This is a
  preliminary analysis that has not yet been validated in the field. Please send ground
  feedback to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/water-extents-in-midongy-atsimo-district-atsimo-atsinanana-region-madagascar-as-of-24-febr]'
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
      areas based on WorldPop data
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "Sentinel-2 satellite imagery from 24 February 2022 was analyzed by\
    \ UNOSAT to detect surface water extents through visual interpretation and multi-temporal\
    \ comparison. Detected water polygons (90 km\xB2 total) were intersected with\
    \ WorldPop population grids to estimate approximately 5,000 people potentially\
    \ exposed to flooded areas in the 1,200 km\xB2 study area."
  sources:
  - id: source_1
    license: null
    name: Sentinel-2
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
- href: https://data.humdata.org/dataset/water-extents-in-midongy-atsimo-district-atsimo-atsinanana-region-madagascar-as-of-24-febr
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
  description: Satellite detected water extents in Midongy-Atsimo District, Atsimo
    Atsinanana Region, Madagascar as of 24 February 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220221MDG/TC20220221MDG_gdb.zip
  format: Geodatabase
  id: resource_38194f82
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220221MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Midongy-Atsimo District, Atsimo
    Atsinanana Region, Madagascar as of 24 February 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/MG/TC20220221MDG/TC20220221MDG_SHP.zip
  format: null
  id: resource_39b58440
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20220221MDG_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mdg_unosat_detectedwaterextentsmidon_20220304
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-03-04'
temporal_resolution: null
title: Satellite detected water extents in Midongy-Atsimo District, Atsimo Atsinanana
  Region, Madagascar as of 24 February 2022
version: null
vulnerability: null
---
