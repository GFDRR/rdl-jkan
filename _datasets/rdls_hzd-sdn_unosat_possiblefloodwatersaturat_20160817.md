---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/possible-flood-water-saturated-soil-over-sennar-and-signa-area-sennar-state-sudan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/possible-flood-water-saturated-soil-over-sennar-and-signa-area-sennar-state-sudan
dataset_id: rdls_hzd-sdn_unosat_possiblefloodwatersaturat_20160817
description: 'This map illustrates satellite-detected possible flood water & saturated
  soil over Sennar State, extracted from Radarsar-2 imagery acquired 12 August 2016.
  UNOSAT has analysed the area using a Radarsat-2 image acquired on 12 August 2016
  to identify and delineate the Possible Flood Water & Saturated / Wet Soil. According
  to satellite derived analysis some areas within Sennar State seem to be flooded.
  In addition, and the Blue Nile increased its size especially in the right bank,
  without apparently causing floods inside build up areas.The exact limit of flood
  waters is uncertain because of the low spatial resolution of the satellite data
  used for this analysis. Detected water bodies likely reflect an underestimation
  of all flood-affected areas within the map extent. This analysis has not yet been
  validated in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/possible-flood-water-saturated-soil-over-sennar-and-signa-area-sennar-state-sudan]'
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
  description: UNOSAT analysts processed Radarsat-2 SAR imagery acquired on 12 August
    2016 over Sennar State, Sudan, comparing satellite images to identify and delineate
    areas of possible flood water and saturated/wet soil. The analysis produced vector
    polygons of inundated areas with confidence classifications and field validation
    attributes.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/possible-flood-water-saturated-soil-over-sennar-and-signa-area-sennar-state-sudan
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
  description: Sudan - Possible Flood Water & Saturated Soil over Sennar and Signa
    Area, Sennar State (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20160808SDN/FL20160808SDN.gdb.zip
  format: Geodatabase
  id: resource_89a48de5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160808SDN.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sudan - Possible Flood Water & Saturated Soil over Sennar and Signa
    Area, Sennar State (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SD/FL20160808SDN/FL20160808SDN_shp.zip
  format: null
  id: resource_bdced313
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160808SDN_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sdn_unosat_possiblefloodwatersaturat_20160817
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
  start: '2016-08-17'
temporal_resolution: null
title: Sudan - Possible Flood Water & Saturated Soil over Sennar and Signa Area, Sennar
  State
version: null
vulnerability: null
---
