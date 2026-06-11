---
catalog: World Bank Data Catalog
contact_point:
  email: pchrzanowski@worldbank.org
  id: attribution_contact
  name: Pierre Chrzanowski
  url: https://www.gfdrr.org/en
creator:
  email: James.Allard@jbarisk.com
  id: attribution_creator_jba
  name: JBA Risk Management Limited
  url: https://www.jbarisk.com/
dataset_id: rdls_hel-sle_freetownfloodrisk
description: Complete probabilistic flood risk assessment for Freetown including high-resolution
  hazard maps (1m river and surface water flooding), building exposure data (153,436
  buildings from GEM Foundation GED4ALL), and comprehensive loss metrics (AAL, OEP,
  AEP, ELT, PLT). Commissioned by World Bank to support climate and disaster risk
  management in Sierra Leone.
details: 'This comprehensive flood risk assessment combines: (1) JBA''s high-resolution
  (1m) probabilistic flood hazard maps for both river and surface water flooding across
  6 return periods (RP20-RP1500); (2) GEM Foundation''s building exposure database
  (GED4ALL taxonomy) with 153,436 georeferenced buildings valued at USD $8.08 billion;
  and (3) complete catastrophe modeling loss outputs including Average Annual Loss,
  loss exceedance curves (OEP/AEP), event loss tables (1,943 stochastic events), and
  spatial loss aggregations. Dataset represents industry-standard probabilistic flood
  risk assessment comparable to commercial catastrophe models.'
exposure:
  category: buildings
  dimension: content, structure
  quantity_kind: count, monetary
  taxonomy: GED4ALL
extra_attributions:
- email: msuwa@worldbank.org
  id: attribution_ttl1
  name: Makoto Suwa
  role: world_bank_team_lead
  url: https://www.worldbank.org
- email: csoto@worldbank.org
  id: attribution_ttl2
  name: Claudia Soto
  role: world_bank_team_lead
  url: https://www.worldbank.org
- email: rreid1@worldbank.org
  id: attribution_ttl3
  name: Robert Reid
  role: world_bank_team_lead
  url: https://www.worldbank.org
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: flood
  intensity: wd:m
  occurrence_range: Return periods from 20, 50, 100, 200, 500, and 1,500 years
  processes: fluvial_flood, pluvial_flood
  seasonality: ''
license: CC-BY-4.0
loss:
  approach: ''
  base_data_type: ''
  category: ''
  description: 'AAL aggregated by administrative district (Admin2 level). Western
    Area Urban district accounts for 73.5% of total AAL (USD $594,607) while Western
    Area Rural accounts for 26.5% (USD $214,300). Urban concentration reflects higher
    building density and exposure values in downtown Freetown., AAL disaggregated
    by occupancy classification. Residential buildings account for 98.6% of losses
    (USD $797,345 from 143,261 buildings), Commercial 1.4% (USD $11,247 from 9,522
    buildings), and Industrial 0.04% (USD $314 from 652 buildings). High residential
    loss share reflects both higher building count and higher flood exposure in residential
    areas of Freetown., Aggregate Exceedance Probability (AEP) curve showing total
    annual aggregate losses at return periods from RP2 to RP1000. AEP accounts for
    possibility of multiple flood events occurring in same year, aggregating all event
    losses. Used for portfolio risk assessment and annual loss budgeting., Average
    Annual Loss (AAL) for combined river and surface water flooding in Freetown study
    area. Total AAL: USD $808,905. Calculated from stochastic event set of 1,943 flood
    events using: (1) JBA probabilistic flood hazard maps at 1m resolution (6 return
    periods: RP20-RP1500), (2) GEM Foundation building exposure portfolio (153,436
    buildings valued at USD $8.08 billion with GED4ALL taxonomy), and (3) proprietary
    depth-damage vulnerability functions. AAL represents expected annual building
    damage in ground-up losses. Vulnerability functions are commercial/proprietary
    and not included in this dataset but assumed to follow industry-standard depth-damage
    relationships for building types in GED4ALL taxonomy., Event Loss Table (ELT)
    containing ground-up losses for 1,943 stochastic flood events representing full
    range of possible flood scenarios. Maximum single event loss: USD $135.4 million.
    Mean event loss: USD $4.16 million. 1,775 events (91.4%) produce non-zero losses.
    Used for reinsurance pricing, catastrophe bond modeling, and risk transfer calculations.,
    National Average Annual Loss for Sierra Leone. Total national AAL: USD $101.3
    million. By province: Eastern USD $31.6M (31.2%), Southern USD $29.3M (29.0%),
    North West USD $20.5M (20.2%), Northern USD $17.8M (17.6%), Western Area USD $2.1M
    (2.1%). By occupancy: Residential USD $99.0M (97.8%), Commercial USD $2.2M (2.1%),
    Industrial USD $103K (0.1%). Freetown represents only 0.8% of national AAL. Complete
    probabilistic outputs (OEP, AEP, ELT, PLT) available at national, provincial,
    and district levels., Occurrence Exceedance Probability (OEP) curve showing ground-up
    flood losses at return periods from RP2 to RP1000. Key loss metrics: RP100 = USD
    $13.46M (1% annual probability, regulatory standard), RP500 = USD $60.37M (0.2%
    annual probability, common insurance threshold), RP1000 = USD $82.63M (Probable
    Maximum Loss). OEP represents the maximum loss from a single event in a given
    year at each return period. Used for regulatory capital calculations, Solvency
    II compliance, and insurance/reinsurance pricing decisions., Period Loss Table
    (PLT) showing annual loss distributions across simulated years. Each year contains
    one or more stochastic events sampled from full event set. Used by risk managers
    and CFOs for financial planning, capital allocation, and understanding year-to-year
    loss volatility., Spatial AAL dataset at Admin4 (ward/section) level provided
    as shapefile. 74 wards with AAL ranging from USD $0 (3 wards) to USD $144,276
    (Gloucester ward, highest risk). Total AAL: USD $815,504 (slight difference from
    probabilistic total of USD $808,905 likely due to spatial aggregation methods).
    This spatial dataset enables ward-level investment prioritization and targeted
    risk reduction interventions.'
  dimension: ''
  exposure_id: ''
  hazard_analysis_type: ''
  hazard_id: ''
  hazard_process: fluvial_flood
  hazard_type: flood
  impact_metric: ''
  impact_type: ''
  impact_unit: ''
  type: ''
  vulnerability_id: ''
project:
  name: 'Selection # 1279998 / Consultancy Services to develop capacities and capabilities
    in relation to climate, weather and disaster risk management services in Sierra
    Leone'
  url: https://www.worldbank.org
publisher:
  email: data@gfdrr.org
  id: attribution_publisher
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  url: https://www.gfdrr.org/en
purpose: To support the Government of Sierra Leone and relevant stakeholders in understanding
  comprehensive flood risk, enabling evidence-based investment decisions, insurance/reinsurance
  pricing, and disaster risk management planning for Freetown.
resources:
- coordinate_system: EPSG:4326
  description: "Complete set of high-resolution (1m) probabilistic flood hazard maps\
    \ for Freetown covering both river (fluvial) and surface water (pluvial) flooding.\
    \ Data formats: GeoTIFF (primary raster data), PDF (methodology documentation),\
    \ XML (metadata), OVR (overview pyramids). Contains 12 GeoTIFF rasters (6 return\
    \ periods \xC3\u2014 2 flood types) in WGS84 (EPSG:4326). File naming convention:\
    \ Freetown_202304_{FLRF|FLSW}_U_RP{20|50|100|200|500|1500}_RD_1m_4326.tif where\
    \ FLRF=River Flood, FLSW=Surface Water Flood, U=Undefended. Each GeoTIFF includes\
    \ auxiliary XML metadata and overview (OVR) files. Also includes 2 technical methodology\
    \ PDFs (JBA_Freetown_Sierra_Leone_RiverFloodMap2023.pdf and JBA_Freetown_Sierra_Leone_SurfaceWaterFloodMap2023.pdf)\
    \ documenting modeling approach, hydrological/hydraulic models (JFlow 2D + RFlow\
    \ 1D for river, JFlow 2D only for surface water), data sources (Intermap NEXTMap\
    \ World30 DSM), and model specifications. Flood depth rasters enhanced from 30m\
    \ base resolution to 1m using water filling algorithm. Undefended scenarios model\
    \ flooding without flood defenses or drainage systems."
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066934/DR0095923/2023s0512_Freetown_Flood_Hazard_Maps.zip
  format: GeoTIFF (tif)
  id: resource_freetown_hazard_maps
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Freetown Flood Hazard Maps
- coordinate_system: EPSG:4326
  description: 'Spatial loss datasets and visualization products for Freetown flood
    risk. Data formats: Shapefile (primary spatial data with .shp, .shx, .dbf, .prj,
    .cpg components), PDF (visualization maps). Primary dataset is Admin4-level AAL
    shapefile (Freetown_Admin4_Combined_Flood_AAL.shp) containing Average Annual Loss
    in USD for 74 wards/sections, with values ranging from $0 to $144,276 per ward
    (total AAL: $815,504). Includes 6 PDF visualization maps: AAL choropleth map,
    topographic overview, and RP20/RP100 flood hazard maps (with and without observed
    flood points). Also contains City Council validation data: flash flood observation
    points shapefile (45 locations) and flash flood areas shapefile (8 polygons) used
    for model ground-truthing. Additional vector datasets include RP20 and RP100 flood
    extent polygons. All shapefiles in WGS84 (EPSG:4326) with complete attribute tables.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066934/DR0095922/2023s0512_Freetown_Flood_Hazard_and_Loss_Maps.zip
  format: Shapefile (shp)
  id: resource_freetown_loss_maps
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Freetown Flood Hazard and Loss Maps
- coordinate_system: null
  description: 'Complete catastrophe modeling outputs for Freetown including Average
    Annual Loss (AAL), Occurrence Exceedance Probability (OEP), Aggregate Exceedance
    Probability (AEP), Event Loss Tables (ELT), and Period Loss Tables (PLT). Data
    formats: CSV (primary probabilistic outputs), TXT (summary documentation). Contains
    15 CSV files organized by aggregation level: S1 (by occupancy: residential/commercial/industrial),
    S2 (by study area: Freetown 1m DEM extent), S3 (by district: Western Area Urban/Rural).
    File naming convention: 2023s0512_SLE_Freetown_03_gul_{S1|S2|S3}_{aalcalc|eltcalc|leccalc_wheatsheaf_mean_aep|leccalc_wheatsheaf_mean_oep|pltcalc}.csv.
    Key results: Total AAL $808,905 USD, RP100 loss $13.46M, RP500 loss $60.37M, RP1000
    PML $82.63M. ELT contains 1,943 stochastic flood events with maximum single event
    loss of $135.4M. Includes summary text file explaining aggregation levels and
    methodology. Ground-up losses calculated from JBA hazard maps, GEM exposure portfolio
    (153,436 buildings), and proprietary vulnerability functions.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066934/DR0095924/2023s0512_Freetown_Probabilistic_Analysis_Results.zip
  format: CSV (csv)
  id: resource_freetown_probabilistic
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Freetown Probabilistic Analysis Results
- coordinate_system: EPSG:4326
  description: 'Building exposure datasets used for flood loss modeling. Data formats:
    CSV (primary exposure data), TXT (license and documentation). Contains GEM Foundation
    GED4ALL (Global Exposure Database for All) national data for Sierra Leone: Exposure_Res_Sierra_Leone.csv
    (336 records, 883,521 residential buildings, $38.3B USD), Exposure_Com_Sierra_Leone.csv
    (147 records, 39,418 commercial buildings, $3.0B USD), Exposure_Ind_Sierra_Leone.csv
    (84 records, 3,178 industrial buildings, $288.8M USD). GED4ALL data includes building
    taxonomy, replacement costs, dwelling counts, and occupants per asset at Admin1/Admin2
    levels. Primary loss modeling dataset is Freetown_ptf_v2.csv containing 153,436
    disaggregated building records with precise lat/lon coordinates, Total Insurable
    Value (TIV) in USD, occupancy codes (1050=Residential, 1100=Commercial, 1150=Industrial),
    and peril coverage codes (ORF=River Flood, OSF=Surface Water Flood). Total Freetown
    exposure: $8.08B USD. Also includes SLE_admin2_ptf_output.csv (complete Sierra
    Leone portfolio at Admin2 level). README.txt documents GEM Foundation license
    (CC-BY-NC-SA 4.0) and data lineage from Global Seismic Risk Model.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066934/DR0095925/2023s0512_Modelled_Exposure.zip
  format: CSV (csv)
  id: resource_modelled_exposure
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Modelled Exposure Data
- coordinate_system: null
  description: 'National-level flood risk visualization products for Sierra Leone
    showing Average Annual Loss (AAL) aggregated at different administrative and economic
    levels. Data formats: PDF (primary cartographic products), PNG (AAL by occupancy
    chart). Contains 3 PDF maps and 1 PNG: AAL by province (Admin1: 5 provinces),
    AAL by district (Admin2: 16 districts), AAL by line of business/occupancy (residential/commercial/industrial),
    and national overview. Maps show spatial distribution of USD $101.3M total national
    AAL with provincial breakdown: Eastern $31.6M (31.2%), Southern $29.3M (29.0%),
    North West $20.5M (20.2%), Northern $17.8M (17.6%), Western Area $2.1M (2.1%).
    Cartographic products complement the probabilistic analysis CSV outputs and enable
    strategic national-level flood risk planning.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066934/DR0095926/2023s0512_Sierra_Leone_Flood_Loss_Maps.zip
  format: PDF (pdf)
  id: resource_sle_loss_maps
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Sierra Leone National Flood Loss Maps
- coordinate_system: null
  description: 'Complete national-level catastrophe modeling outputs for Sierra Leone
    including AAL, OEP, AEP, ELT, and PLT at four aggregation levels. Data formats:
    CSV (primary probabilistic outputs), TXT (summary documentation). Contains 20
    CSV files organized as: S1 (national total), S2 (by district/Admin2: 16 districts),
    S3 (by occupancy: residential/commercial/industrial), S4 (by province/Admin1:
    5 provinces). File naming convention: 2023s0512_Sierra Leone_05_gul_{S1|S2|S3|S4}_{aalcalc|eltcalc|leccalc_wheatsheaf_mean_aep|leccalc_wheatsheaf_mean_oep|pltcalc}.csv.
    Key results: National AAL $101.3M USD, occupancy breakdown showing 97.8% residential
    ($99.0M), 2.1% commercial ($2.2M), 0.1% industrial ($103K). Complete stochastic
    event sets and loss distributions enable national-level portfolio risk assessment,
    reinsurance pricing, and disaster risk financing. Includes summary text file documenting
    aggregation structure. Freetown (Western Area) represents only 0.8% of national
    AAL, indicating significant rural and other urban flood risk exists across Sierra
    Leone.'
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0066934/DR0095927/2023s0512_Sierra_Leone_Probabilistic_Analysis_Results.zip
  format: CSV (csv)
  id: resource_sle_probabilistic
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Sierra Leone National Probabilistic Analysis Results
risk_data_type:
- hazard
- exposure
- loss
schema: rdl-03
slug: rdls_hel-sle_freetownfloodrisk
spatial:
  bbox:
  - -13.303192
  - 8.3417096
  - -13.115017
  - 8.5038197
  countries:
  - SLE
  gazetteer_entries:
  - description: Freetown
    id: gazetteer_freetown
    scheme: GEONAMES
    uri: https://www.geonames.org/2409306/freetown.html
  scale: sub-national
title: Comprehensive Flood Risk Assessment for Freetown, Sierra Leone
version: '1.0'
vulnerability: null
---
