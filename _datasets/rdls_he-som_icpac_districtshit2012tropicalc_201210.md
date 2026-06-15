---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2012-tropical-cyclone-murjan
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2012-tropical-cyclone-murjan
dataset_id: rdls_he-som_icpac_districtshit2012tropicalc_201210
description: 'This layer shows Somalia Districts struck by 2012 TC Murjan. They include,
  Bossaso, Bandarbeyla, Iskushuban, Garoowe and Eyl District. TC Murjan formed over
  the south Arabian Sea in association with an active inter tropical convergence zone
  during last week of October 2012. Moving west-southwestwards, it crossed Somalia
  coast between 1700 and 1800 UTC of 25th October near lat. 9.80N and long. 50.80E.
  The system could maintain its intensity of cyclonic storm till landfall, basically
  due to low to moderate vertical wind shear. TC Murjan caused heavy rainfall and
  strong wind over Somalia. The storm produced maximum wind speeds of 68.4Km/hr(40.2mph)
  and rainfall amounts of (100-200)mm. Flash flooding washed away livestock and bridges
  in the Bari region, causing some fatalities. 100,000 livestock were reported to
  have died as a result of the storm. After the landfall, due to land interaction,
  it weakened into a deep depression over coastal Somalia at 1800 UTC of 25th October.
  It further weakened into a depression over Somalia in the morning of 26th October
  while moving west-southwest wards. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2012-tropical-cyclone-murjan]'
details: null
exposure:
- asset_type:
    description: Population residing in Somalia districts affected by TC Murjan
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
    strong_wind:
    - analysis_type: probabilistic
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "ICPAC documented the observed tropical cyclone Murjan event from October\
    \ 2012, recording its formation over the Arabian Sea, westward track, and landfall\
    \ near 9.80\xB0N, 50.80\xB0E on the Somalia coast. The dataset identifies five\
    \ districts struck by the cyclone and its associated heavy rainfall and strong\
    \ wind impacts, compiled into geospatial administrative boundary layers."
  sources:
  - id: source_1
    license: null
    name: IGAD Climate Prediction and Applications Center (ICPAC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2012-tropical-cyclone-murjan
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2012_TCMurjan&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. This layer shows Somalia Districts struck by 2012 TC Murjan.
    They include, Bossaso, Bandarbeyla, Iskushuban, Garoowe and Eyl District. TC Murjan
    formed over the south Arabian Sea in association with an active inter tropical
    convergence zone during last week of October 2012. Moving west-southwestwards,
    it crossed Somalia coast between 1700 and 1800 UTC of 25th October near lat. 9.80N
    and long. 50.80E. The system could maintain its intensity of cyclonic storm till
    landfall, basically due to low to moderate vertical wind shear.
  download_url: null
  format: null
  id: resource_bb43e648
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2012 Tropical Cyclone Murjan CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2012_TCMurjan&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. This layer shows Somalia Districts struck by 2012 TC Murjan.
    They include, Bossaso, Bandarbeyla, Iskushuban, Garoowe and Eyl District. TC Murjan
    formed over the south Arabian Sea in association with an active inter tropical
    convergence zone during last week of October 2012. Moving west-southwestwards,
    it crossed Somalia coast between 1700 and 1800 UTC of 25th October near lat. 9.80N
    and long. 50.80E. The system could maintain its intensity of cyclonic storm till
    landfall, basically due to low to moderate vertical wind shear.
  download_url: null
  format: null
  id: resource_133e6e4b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2012 Tropical Cyclone Murjan Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2012_TCMurjan&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. This layer shows Somalia Districts struck by 2012 TC
    Murjan. They include, Bossaso, Bandarbeyla, Iskushuban, Garoowe and Eyl District.
    TC Murjan formed over the south Arabian Sea in association with an active inter
    tropical convergence zone during last week of October 2012. Moving west-southwestwards,
    it crossed Somalia coast between 1700 and 1800 UTC of 25th October near lat. 9.80N
    and long. 50.80E. The system could maintain its intensity of cyclonic storm till
    landfall, basically due to low to moderate vertical wind shear.
  download_url: null
  format: null
  id: resource_05643ccd
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2012 Tropical Cyclone Murjan GeoJSON
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2012_TCMurjan&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. This layer shows Somalia Districts struck by
    2012 TC Murjan. They include, Bossaso, Bandarbeyla, Iskushuban, Garoowe and Eyl
    District. TC Murjan formed over the south Arabian Sea in association with an active
    inter tropical convergence zone during last week of October 2012. Moving west-southwestwards,
    it crossed Somalia coast between 1700 and 1800 UTC of 25th October near lat. 9.80N
    and long. 50.80E. The system could maintain its intensity of cyclonic storm till
    landfall, basically due to low to moderate vertical wind shear.
  download_url: null
  format: null
  id: resource_cface35f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2012 Tropical Cyclone Murjan Zipped Shapefile
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-som_icpac_districtshit2012tropicalc_201210
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2012-10-26'
  start: '2012-10-23'
temporal_resolution: null
title: Somalia Districts hit by 2012 Tropical Cyclone Murjan
version: null
vulnerability: null
---
