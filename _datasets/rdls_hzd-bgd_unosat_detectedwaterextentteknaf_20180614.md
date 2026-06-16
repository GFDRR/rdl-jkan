---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-teknaf-upazila-cox-s-bazar-district-chittagong-division-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-teknaf-upazila-cox-s-bazar-district-chittagong-division-
dataset_id: rdls_hzd-bgd_unosat_detectedwaterextentteknaf_20180614
description: 'This map illustrates satellite-detected surface water extent in Teknaf
  Upazila, District of Cox''s Bazar, Chittagong Division, located in the southeastern
  part of Bangladesh as detected using a Sentinel-1 satellite image acquired on the
  13 June 2018 compared to a Sentinel-1 satelllite image acquired on 22 May 2018.
  The total analysed area is about 5,000 ha, and about 1,600 ha of surface waters
  could be observed on 13th of June 2018 whereas 1,050 ha were observed on 22 May
  2018. The increase of observed surface waters in this area is about 50 %. Within
  the camps'' extents, 52 ha of water were detected and the most affected seems to
  be camp 25. Please note that in many zones, the affected lands are mainly agricultural
  and open areas. It is likely that flood waters have been systematically underestimated
  along highly vegetated areas along main river banks and within built-up urban areas
  because of the special characteristics of the satellite data used. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-in-teknaf-upazila-cox-s-bazar-district-chittagong-division-]'
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
  description: Sentinel-1 SAR satellite images from 22 May 2018 and 13 June 2018 were
    acquired and analyzed by UNOSAT analysts through visual comparison to detect changes
    in surface water extent. Water bodies were delineated and quantified by area (hectares)
    within the 5,000 ha study area in Teknaf Upazila, with results stored as polygon
    geometries with associated metadata including confidence levels and field validation
    notes.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-in-teknaf-upazila-cox-s-bazar-district-chittagong-division-
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
  description: Satellite Detected Water Extent in Teknaf Upazila, Cox's Bazar District,
    Chittagong Division, Bangladesh (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20180518BGD/FL20180518BGD_SHP.zip
  format: null
  id: resource_ca4626ee
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180518BGD_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bgd_unosat_detectedwaterextentteknaf_20180614
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-06-14'
temporal_resolution: null
title: Satellite Detected Water Extent in Teknaf Upazila, Cox's Bazar District, Chittagong
  Division, Bangladesh
version: null
vulnerability: null
---
