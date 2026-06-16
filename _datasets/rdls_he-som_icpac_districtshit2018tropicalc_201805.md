---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2018-tropical-cyclone-saga
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2018-tropical-cyclone-saga
dataset_id: rdls_he-som_icpac_districtshit2018tropicalc_201805
description: '2018 Tropical Cyclone Saga struck several districts in Somalia. These
  include Bai, Lughaye, Zeylac, Laasqoray, Bossaso, Caluula, Iskushuban, Qardho and
  Garoowe District. TC Sagar originated from Yemen where it had caused flooding and
  wind damage. On 19 May, 2018 TC Sagar made landfall in north-western Somaliland.
  It moved with wind gusts of up to 120 km/hour that delivered a year&rsquo;s worth
  of rain to some areas that is between 150 and 200mm in some parts of the north.
  Villages struck by the storm include Lughaya, Zeila, Baki, Bareeda, Caluula, Murcanyo,
  Gumbax and Xaabo. On 19 May, TC Sagar made landfall in western Somaliland, impacting
  close to 170,000 people, mainly in Awdal region. The storm destroyed crops, shelters
  and social service infrastructure, including water, health, nutrition, and education
  facilities. The Somaliland authorities estimated 50 people died and seven were still
  missing. In Somaliland, at least 16 people died in Galbeed and Awdal, where the
  cyclone made landfall. Three quarters of the livestock were killed along with major
  damage of water systems and health facilities and 39 schools were damaged or destroyed
  with a major impact on children. Summary of the storm''s impacts according to districts:
  Galbeed, Laasqoray, Qardho, Ishkushban, Bossaso, Garowe People displaced: 1,780
  families People affected: 669,000 Houses destroyed: 80 families Death: 52 People
  Injured: 12 Missing persons: 27(Mainland) and 4(Fishermen) Disrupted services: 5
  in Bossaso and Garoowe Bareeda, Caluula, Murcanyo, Gumbax, and some parts of Xaabo
  People Missing: In Puntland 35 houses, 15 small boats. In Tawakal, 220 improvised
  houses for IDPS were washed away. 30 boats in Caluula and 20 small boats in Bosaso
  seaport. In Berber 125 families. In Ceel Sheekh, 15 shelters destroyed. Livestock
  lost: In Puntland 56 camels, nearly 1,260 goats and sheep and 19 donkeys died..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2018-tropical-cyclone-saga]'
details: null
exposure:
- asset_type:
    description: Population in districts and villages affected by TC Saga in Somalia
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
- asset_type:
    description: Infrastructure and settlements in affected districts including villages
      of Lughaya, Zeila, Baki, Bareeda, Caluula, Murcanyo, Gumbax and Xaabo
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
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
  description: Post-event observational data compiled by ICPAC documenting the geographic
    extent and physical characteristics of TC Saga's impact across Somali districts
    on 19 May 2018, including measured wind gusts (120 km/h) and rainfall totals (150-200
    mm), with affected areas delineated at the district and village level.
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
- href: https://data.humdata.org/dataset/icpac-geonode-somalia-districts-hit-by-2018-tropical-cyclone-saga
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2018_TCSaga&outputFormat=csv&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: CSV file. 2018 Tropical Cyclone Saga struck several districts in Somalia.
    These include Bai, Lughaye, Zeylac, Laasqoray, Bossaso, Caluula, Iskushuban, Qardho
    and Garoowe District. TC Sagar originated from Yemen where it had caused flooding
    and wind damage. On 19 May, 2018 TC Sagar made landfall in north-western Somaliland.
    It moved with wind gusts of up to 120 km/hour that delivered a year&rsquo;s worth
    of rain to some areas that is between 150 and 200mm in some parts of the north.
    Villages struck by the storm include Lughaya, Zeila, Baki, Bareeda, Caluula, Murcanyo,
    Gumbax and Xaabo.
  download_url: null
  format: null
  id: resource_98e850a8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2018 Tropical Cyclone Saga CSV
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2018_TCSaga&outputFormat=excel&srs=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Excel file. 2018 Tropical Cyclone Saga struck several districts in
    Somalia. These include Bai, Lughaye, Zeylac, Laasqoray, Bossaso, Caluula, Iskushuban,
    Qardho and Garoowe District. TC Sagar originated from Yemen where it had caused
    flooding and wind damage. On 19 May, 2018 TC Sagar made landfall in north-western
    Somaliland. It moved with wind gusts of up to 120 km/hour that delivered a year&rsquo;s
    worth of rain to some areas that is between 150 and 200mm in some parts of the
    north. Villages struck by the storm include Lughaya, Zeila, Baki, Bareeda, Caluula,
    Murcanyo, Gumbax and Xaabo.
  download_url: null
  format: null
  id: resource_4fcb8d9b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2018 Tropical Cyclone Saga Excel
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2018_TCSaga&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: Zipped Shapefile file. 2018 Tropical Cyclone Saga struck several districts
    in Somalia. These include Bai, Lughaye, Zeylac, Laasqoray, Bossaso, Caluula, Iskushuban,
    Qardho and Garoowe District. TC Sagar originated from Yemen where it had caused
    flooding and wind damage. On 19 May, 2018 TC Sagar made landfall in north-western
    Somaliland. It moved with wind gusts of up to 120 km/hour that delivered a year&rsquo;s
    worth of rain to some areas that is between 150 and 200mm in some parts of the
    north. Villages struck by the storm include Lughaya, Zeila, Baki, Bareeda, Caluula,
    Murcanyo, Gumbax and Xaabo.
  download_url: null
  format: null
  id: resource_92e64a88
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2018 Tropical Cyclone Saga Zipped Shapefile
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aa__2018_TCSaga&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoJSON file. 2018 Tropical Cyclone Saga struck several districts in
    Somalia. These include Bai, Lughaye, Zeylac, Laasqoray, Bossaso, Caluula, Iskushuban,
    Qardho and Garoowe District. TC Sagar originated from Yemen where it had caused
    flooding and wind damage. On 19 May, 2018 TC Sagar made landfall in north-western
    Somaliland. It moved with wind gusts of up to 120 km/hour that delivered a year&rsquo;s
    worth of rain to some areas that is between 150 and 200mm in some parts of the
    north. Villages struck by the storm include Lughaya, Zeila, Baki, Bareeda, Caluula,
    Murcanyo, Gumbax and Xaabo.
  download_url: null
  format: null
  id: resource_fd869a54
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia Districts hit by 2018 Tropical Cyclone Saga GeoJSON
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-som_icpac_districtshit2018tropicalc_201805
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
  end: '2018-05-20'
  start: '2018-05-19'
temporal_resolution: null
title: Somalia Districts hit by 2018 Tropical Cyclone Saga
version: null
vulnerability: null
---
