---
attributions:
- entity:
    affiliation: null
    email: null
    name: Satellite imagery (optical and SAR sensors)
    url: https://data.humdata.org/dataset/priority-index-sri-lanka-floods-may-2017
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Human settlement geo-data
    url: https://data.humdata.org/dataset/priority-index-sri-lanka-floods-may-2017
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/priority-index-sri-lanka-floods-may-2017
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/priority-index-sri-lanka-floods-may-2017
dataset_id: rdls_hel-lka_nlrc510_priorityindexfloodsmay201_20170601
description: "Product This priority index was derived by combining a detailed flood\
  \ extent mapping with detailed human settlement geo-data. Both sources were combined\
  \ to produce the location and magnitude of population living in flooded areas. This\
  \ was subsequently aggregated to admin-4 areas (GND) as well as admin-3 areas (DS\
  \ divisional). The flood extent mapping was derived in turn by combining two sources:\
  \ Flood extent maps could be produced rather faster using satellite imageries captured\
  \ by either optical sensors or Synthetic Aperture Radar (SAR) sensors. In most places\
  \ flood is cause by heavy rainfall which means in most cases cloud is present, this\
  \ is a limitation for optical sensors as they can't penetrate clouds. Radar sensors\
  \ are not affected by cloud, which make them more useful in presence of cloud. In\
  \ This analysis we analyzed sentinel2 optical image from May 28th and Sentinel 1\
  \ SAR image from May 30th. Then we combine the two results adding up the flood extents.\
  \ Main cloud covered areas and permanent water bodies are removed from the flood\
  \ extent map using the Sentinel 2 cloud mask. The scale/resolution of the flood\
  \ extent map is 30mts where as the permanent water body map has 250m scale resolution.\
  \ This will introduce some discrepancy: part of flood extent map could be permanent\
  \ water body. Scope Analysis focused on 4 districts in South-West Sri Lanka based\
  \ on news reports (https://www.dropbox.com/s/n0qdqe7qfgq6fyv/special_situation.pdf?dl=0).\
  \ Based on the admin-3-level analysis, highest percentages of population living\
  \ in flooded areas were seen in Matara district. Admin-4 level analysis concentrated\
  \ only on Matara district for that reason. Caveats The dataset is showing percentage\
  \ flooded. The data has not yet been corrected for small populations. We believe\
  \ the product is currently pointing to the high priority areas. In the shp or csv\
  \ files the user of this data could easily correct for small populations, if there\
  \ is a wish to target on the amount of people affected. Data used from partners\
  \ The human settlement data was retrieved from http://ciesin.columbia.edu/data/hrsl/.\
  \ Facebook Connectivity Lab and Center for International Earth Science Information\
  \ Network - CIESIN - Columbia University. 2016. High Resolution Settlement Layer\
  \ (HRSL). Source imagery for HRSL \xC2\xA9 2016 DigitalGlobe. Accessed 01-06-2017.\
  \ The Radar imagery analysis was done by NASA JPL, whose input in this product has\
  \ been crucial. Visualization An example map is available here: http://bit.ly/SriLankaFloodMap\
  \ Linked data Admin boundaries 3 and 4 can be found here (link on OBJECT_ID): https://data.humdata.org/group/lka?q=&ext_page_size=25&sort=score+desc%2C+metadata_modified+desc&tags=administrative+boundaries#dataset-filter-start\
  \ How to use The ratio column in the SHPs or CSVs can be multiplied by 100 to get\
  \ the percentage of flooding in the area.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/priority-index-sri-lanka-floods-may-2017]"
details: The dataset is showing percentage flooded. The data has not yet been corrected
  for small populations. We believe the product is currently pointing to the high
  priority areas. In the shapefile and csv file the user of this data could easily
  correct for small populations, if there is a wish to target on the volume of people
  affected.
exposure:
- asset_type:
    description: Human settlement population inventory geo-referenced to flood-affected
      areas
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Flood extent was mapped using satellite imagery (optical and SAR sensors)
    for the May 2017 event in Sri Lanka. This was intersected with detailed human
    settlement geo-data to identify population living in flooded areas. Results were
    aggregated to administrative-4 (GND) and administrative-3 (DS divisional) levels
    to produce a priority index for humanitarian response.
  sources:
  - id: source_1
    license: null
    name: Satellite imagery (optical and SAR sensors)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Human settlement geo-data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/priority-index-sri-lanka-floods-may-2017
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population living in flooded areas aggregated to administrative divisions
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: http://ciesin.columbia.edu/data/hrsl/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood extent. Combination of two sources (radar and optical). See description.
  download_url: https://data.humdata.org/dataset/21b40c8e-a436-494e-80a5-70c3eb0228d0/resource/40ae3445-05b6-4264-b06e-d4bf6e77b780/download/flood_srilanka_new.zip
  format: null
  id: resource_40ae3445
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: flood_srilanka_new.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Population living in flooded area per admin-3 area (DSD) for 4 districts
    in South-West Sri Lanka.
  download_url: https://data.humdata.org/dataset/21b40c8e-a436-494e-80a5-70c3eb0228d0/resource/c7c3eed1-0fb6-409a-96ee-1dcff2db1da5/download/srilankafloods_priorityindex_admin3_4districts.csv
  format: null
  id: resource_c7c3eed1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SriLankaFloods_PriorityIndex_admin3_4districts.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Population living in flooded area per admin-4 area (GND) for Matara
    district in Southern Sri Lanka.
  download_url: https://data.humdata.org/dataset/21b40c8e-a436-494e-80a5-70c3eb0228d0/resource/9f0d425b-9105-46e2-978f-2e52bdd990f1/download/srilankafloods_priorityindex_admin4_matara.csv
  format: null
  id: resource_9f0d425b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SriLankaFloods_PriorityIndex_admin4_Matara.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Population living in flooded area per admin-3 area (DSD) for 4 districts
    in South-West Sri Lanka.
  download_url: https://data.humdata.org/dataset/21b40c8e-a436-494e-80a5-70c3eb0228d0/resource/af1d53cf-8162-42e2-95de-1e2420060007/download/admin3_4districts.zip
  format: null
  id: resource_af1d53cf
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: admin3_4districts.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Population living in flooded area per admin-4 area (GND) for Matara
    district in Southern Sri Lanka.
  download_url: https://data.humdata.org/dataset/21b40c8e-a436-494e-80a5-70c3eb0228d0/resource/5adada77-edde-4afe-9a8b-e6997d3bf3d2/download/admin4_matara.zip
  format: null
  id: resource_5adada77
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: admin4_matara.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-lka_nlrc510_priorityindexfloodsmay201_20170601
spatial:
  bbox: null
  centroid: null
  countries:
  - LKA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-06-01'
temporal_resolution: null
title: Priority Index Sri Lanka Floods May 2017
version: null
vulnerability: null
---
