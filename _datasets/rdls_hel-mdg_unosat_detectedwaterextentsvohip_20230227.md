---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extents-in-vohipeno-district-vatovavy-fitovinany-region-madagascar-as-of-23-february
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: TerraSAR-X
    url: https://data.humdata.org/dataset/water-extents-in-vohipeno-district-vatovavy-fitovinany-region-madagascar-as-of-23-february
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-vohipeno-district-vatovavy-fitovinany-region-madagascar-as-of-23-february
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-vohipeno-district-vatovavy-fitovinany-region-madagascar-as-of-23-february
dataset_id: rdls_hel-mdg_unosat_detectedwaterextentsvohip_20230227
description: 'UNOSAT code TC20230221MDG, GDACS Id: 1000961 This map illustrates satellite-detected
  water in Vohipeno district, Vatovavy Fitovinany region, Madagascar from a TerraSAR-X
  imagery acquired on 23 February 2023 at 05:19 local time. Within the analyzed area
  of about 1,100 km2, about 40 km2 of land appear to be flooded. Based on Worldpop
  population data and the detected surface waters, about 231,000 people live within
  the analysed area while 10,000 people are potentially exposed or living close to
  flooded areas. This is a preliminary analysis and has not yet been validated in
  the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT).
  Important note: Flood analysis from radar images may underestimate the presence
  of standing waters in built-up areas and densely vegetated areas due to the backscattering
  properties of the radar signal.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-vohipeno-district-vatovavy-fitovinany-region-madagascar-as-of-23-february]'
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
    description: Total population of 231,000 people within the analyzed area, with
      10,000 people potentially exposed to flooded areas
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed TerraSAR-X SAR imagery acquired on 23 February\
    \ 2023 to detect water surface extents through change detection analysis. Detected\
    \ flood areas (~40 km\xB2) were intersected with WorldPop gridded population data\
    \ to estimate population exposure within the 1,100 km\xB2 study area of Vohipeno\
    \ District, Madagascar."
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: TerraSAR-X
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-in-vohipeno-district-vatovavy-fitovinany-region-madagascar-as-of-23-february
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed or living close to satellite-detected
      flooded areas
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
  description: Satellite-detected water extents in Vohipeno District, Vatovavy Fitovinany
    Region, Madagascar as of 23 February 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3508/TC20230221MDG_gdb.zip
  format: Geodatabase
  id: resource_ee23ffa4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230221MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite-detected water extents in Vohipeno District, Vatovavy Fitovinany
    Region, Madagascar as of 23 February 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3508/TC20230221MDG_SHP.zip
  format: null
  id: resource_016de3de
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230221MDG_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mdg_unosat_detectedwaterextentsvohip_20230227
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
  start: '2023-02-27'
temporal_resolution: null
title: Satellite-detected water extents in Vohipeno District, Vatovavy Fitovinany
  Region, Madagascar as of 23 February 2023
version: null
vulnerability: null
---
