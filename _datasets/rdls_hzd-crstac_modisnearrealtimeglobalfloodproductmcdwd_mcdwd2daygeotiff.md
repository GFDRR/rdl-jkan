---
attributions: []
catalog: NASA Earth Data
contact_point:
  affiliation: null
  email: null
  name: NASA
  url: https://search.earthdata.nasa.gov/search?portal=idn&p=C2018623526-LANCEMODIS&pg%5B0%5D%5Bv%5D=f&pg%5B0%5D%5Bgsk%5D=-start_date&q=MCDWD
creator:
  affiliation: null
  email: null
  name: NASA
  url: https://search.earthdata.nasa.gov/search?portal=idn&p=C2018623526-LANCEMODIS&pg%5B0%5D%5Bv%5D=f&pg%5B0%5D%5Bgsk%5D=-start_date&q=MCDWD
dataset_id: rdls_hzd-crstac_modisnearrealtimeglobalfloodproductmcdwd_mcdwd2daygeotiff
description: 'The MODIS/Aqua+Terra Global Flood Product L3 Near Real Time (NRT) 250m
  2-day GeoTIFF Product (MCDWD_L3_F2_NRT) (beta) provides maps of flooding globally.
  The Global Flood product is provided over 3 compositing periods (1-day, 2-day, and
  3-day) to minimize the impact of clouds and more rigorously identify flood water
  (the best composite will depend on the cloudiness for a particular event). The MCDWD_L3_F2_NRT
  is 2-day product which is generated from current and previous day''s data. Also
  covers processes: coastal_flood, pluvial_flood (STAC subcategory: "coastal flood,fluvial
  flood,pluvial flood") [Source: This metadata record was automatically extracted
  from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: simulated
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
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: The Flood Product is a daily, near-global, ~250 m resolution product
    showing flood and surface water detected from the twice-daily overpass of the
    MODIS optical sensors (onboard Terra and Aqua satellites). To minimize false-positives
    from cloud and terrain shadows, we employ a multi-observation compositing approach,
    and generate the product over three compositing periods (1-day, 2-day, and 3-day).
  sources:
  - id: source_underlying_1
    license: null
    name: MODIS satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: NASA
  url: https://search.earthdata.nasa.gov/search?portal=idn&p=C2018623526-LANCEMODIS&pg%5B0%5D%5Bv%5D=f&pg%5B0%5D%5Bgsk%5D=-start_date&q=MCDWD
purpose: user account needed for data download
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: ref_pub_publicationlink
  name: Publication link
  url: https://www.earthdata.nasa.gov/s3fs-public/2024-04/MCDWD_UserGuide_RevD.pdf
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/flood/modis-near-real-time-global-flood-product-mcdwd/mcdwd-2-day-geotiff/mcdwd-2-day-geotiff.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Item metadata record for this dataset, hosted as part of
    the climate-risk-stac catalogue. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_item
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: MODIS Near Real-Time Global Flood Product (MCDWD) - MCDWD 2-day
    GeoTIFF'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: MODIS Near Real-Time Global Flood Product (MCDWD) - MCDWD 2-day GeoTIFF
    - data file
  download_url: https://dx.doi.org/10.5067/MODIS/MCDWD_L3_F2_NRT.061
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MODIS Near Real-Time Global Flood Product (MCDWD) - MCDWD 2-day GeoTIFF -
    data file
- access_url: https://www.earthdata.nasa.gov/s3fs-public/2024-04/MCDWD_UserGuide_RevD.pdf
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: MODIS Near Real-Time Global Flood Product (MCDWD) - MCDWD 2-day GeoTIFF
    (Publication link)
  download_url: null
  format: Web reference
  id: resource_link_publicationlink
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Publication link
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-crstac_modisnearrealtimeglobalfloodproductmcdwd_mcdwd2daygeotiff
spatial:
  bbox:
  - -180.0
  - -50.0
  - 180.0
  - 70.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 250
temporal:
  central_year: null
  duration: null
  end: '2026'
  start: '2021'
temporal_resolution: P1D
title: MODIS Near Real-Time Global Flood Product (MCDWD) - MCDWD 2-day GeoTIFF
version: null
vulnerability: null
---
